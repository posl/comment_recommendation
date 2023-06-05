def solve():
    h, w = map(int, input().split())
    s = []
    t = []
    for i in range(h):
        s.append(list(input()))
    for i in range(h):
        t.append(list(input()))
    s.sort()
    t.sort()
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print("No")
                return
    print("Yes")
