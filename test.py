arr = sorted(set(map(lambda x: int(x), "-2 0 -6 3 4 5 8 1 2".rstrip().split())))

def get_num():
    arr = list(map(lambda x: int(x), input().rstrip().split()))
    if not arr:
        return None
    else:
        num_set = set(arr)
        num_list = list(num_set)
        num_list.sort()

        for i in range(0, len(num_list)-1):
            if num_list[0] > 1 or num_list[0] < 0:
                return 1
            if (num_list[i+1] - num_list[i]) > 1:
                return num_list[i]+1
#print(get_num())

def seq(arr):
    if len(arr) == 3:
        mid = (len(arr)//2)+1
    else:
        mid = len(arr)//2
    min_num = arr[0]
    if sum(arr[:mid]) != sum(range(min_num,mid+min_num)):
        if arr[:mid][-1] > 1 and min_num < 0:
            if 1 not in arr[:mid]:
                return seq(arr[:mid])
        elif arr[:mid][-1] > 1 and min_num > 1:
            return min_num+1
    if sum(arr[mid:]) == sum(range(arr[mid],len(arr[mid:])+arr[mid])):
        return 1
    if len(arr) == 2:
        while min_num < 0:
            min_num+=1
        return min_num+1
    return seq(arr[mid-1:])
        
print(seq(arr))
        