def solve():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(n):
        if s[i] == t[i]:
            print("No")
            exit()
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == t[j] and s[j] == t[i]:
                print("No")
                exit()
    print("Yes")
