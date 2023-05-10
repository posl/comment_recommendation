def solve():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(n)]
    s.sort()
    t.sort()
    s = list(map(list, zip(*s)))
    t = list(map(list, zip(*t)))
    if s[0] == t[0]:
        for i in range(n):
            for j in range(n):
                if s[0][i] + s[1][j] == t[0][0] + t[1][0] and s[1][i] + s[0][j] == t[1][0] + t[0][0]:
                    print("Yes")
                    return
        print("No")
    else:
        print("No")
    return
