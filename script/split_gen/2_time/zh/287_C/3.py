def problem287_b():
    n,m = map(int, input().split())
    s_list = []
    for i in range(n):
        s_list.append(input())
    t_list = []
    for i in range(m):
        t_list.append(input())
    count = 0
    for i in range(n):
        for j in range(m):
            if s_list[i][-3:] == t_list[j]:
                count += 1
    print(count)
