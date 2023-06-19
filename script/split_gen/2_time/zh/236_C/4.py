def solve():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    s_dict = {}
    for i in range(n):
        s_dict[s[i]] = i
    t_dict = {}
    for i in range(m):
        t_dict[t[i]] = i
    for i in range(n):
        if s[i] in t_dict:
            print("Yes")
        else:
            print("No")
