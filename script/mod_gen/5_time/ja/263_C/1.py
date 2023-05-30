def list_search(n, m, l):
    if n == 1:
        for i in range(1, m + 1):
            l.append(str(i))
        print(' '.join(l))
    else:
        for i in range(1, m + 1):
            l.append(str(i))
            list_search(n - 1, m, l)
            l.pop()
n, m = map(int, input().split())
l = []
list_search(n, m, l)
