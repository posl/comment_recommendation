def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        s, c = map(int, input().split())
        if s in d:
            if d[s] != c:
                print(-1)
                return
        else:
            d[s] = c
    if 1 in d and d[1] == 0:
        print(-1)
        return
    for i in range(1, n+1):
        if i in d:
            print(d[i], end="")
        else:
            if i == 1:
                print(1, end="")
            else:
                print(0, end="")
    print()
