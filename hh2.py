def get_num():
    n = list(map(lambda x: int(x), input().rstrip().split()))
    min_num = min(n)
    max_num = max(n)
    for i in range(min_num, max_num):
        if i>0 and i not in n:
            return i
    return 1

print(get_num())