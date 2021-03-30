import tkinter as tk
from tkinter import Label, ttk
from threading import Thread
from publishers.piter import get_books as p_books
from publishers.williams import get_books as w_books
from publishers.dmkpress import get_books as d_books
from publishers.nostarch import get_books as n_books
from publishers.nit import get_books as nit_books


book_publishers = {
    "Питер": p_books, 
    "Вильямс": w_books, 
    "Dmk press": d_books,   
    "No Starch Press":n_books, 
    "Наука и техника":nit_books,
}


class Application(tk.Frame):
    def __init__(self, master=None):
        self.threads = []
        tk.Frame.__init__(self, master)
        self.grid()

        self.create_option_frame()
        self.create_result_frame()

    def create_option_frame(self):
        option_fr = tk.LabelFrame(
            self,
            text="Опции",
            bd=2,
            padx=5,
            pady=5,
        )
        option_fr.grid(column=0, row=0, sticky=tk.N + tk.S)
        option_fr.grid_propagate(0)
        publisher_lbl = ttk.Label(option_fr, text="Выбор издателя")
        publisher_lbl.pack()
        self.publisher = ttk.Combobox(option_fr, state="readonly")
        self.publisher["values"] = list(book_publishers.keys())
        self.publisher.current(0)
        self.publisher.pack()

        self.load_btn = ttk.Button(
            option_fr, text="Загрузить", command=self.run_load_thread
        )
        self.load_btn.pack()

    def create_result_frame(self):
        result_fr = tk.LabelFrame(self, text="Список", bd=2, padx=5, pady=5)
        result_fr.grid(column=1, row=0)
        # result_fr.grid_propagate(0)
        self.listbox = tk.Listbox(result_fr, height=25, width=100)
        self.listbox.pack()

    def run_load_thread(self):
        self.load_btn.config(state="disabled")
        self.threads.append(Thread(target=self.update_books))
        self.threads[-1].setDaemon(True)
        self.threads[-1].start()

    def serialize_info(self, data_dict: dict):
        result_list = []
        for k, v in data_dict.items():
            result_list.append(f"=== {k} ===")
            result_list.extend(v)
            result_list.append(" ")
        return result_list

    def fill_listbox(self, books: list):
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, *books)

    def update_books(self):
        publisher = self.publisher.get()
        books_data = book_publishers[publisher]()
        serialized_book_list = self.serialize_info(books_data)
        self.fill_listbox(serialized_book_list)
        self.load_btn.config(state="enabled")


app = Application()
app.master.iconbitmap("./files/ico_32.ico")
app.master.resizable(0, 0)
app.master.minsize(500, 250)
app.master.title("Новинки книго-издательств")
app.mainloop()
