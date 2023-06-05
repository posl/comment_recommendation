def get_input():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = input().split()
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    return n, a, b
