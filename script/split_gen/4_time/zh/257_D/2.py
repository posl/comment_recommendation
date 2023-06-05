def get_input():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input().split(' '))
    return n, arr
