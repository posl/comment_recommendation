def solve():
    n, m = map(int, input().split())
    s_list = input().split()
    t_list = input().split()
    s_dict = {}
    t_dict = {}
    for i in range(n):
        s_dict[s_list[i]] = i
    for i in range(m):
        t_dict[t_list[i]] = i
    for i in range(n):
        if s_dict[s_list[i]] == t_dict[s_list[i]]:
            print("Yes")
        else:
            print("No")
