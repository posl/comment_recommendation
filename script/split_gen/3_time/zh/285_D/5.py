def change_handle(n, s, t):
    # n = int(input())
    # s = []
    # t = []
    # for i in range(n):
    #     s.append(input())
    #     t.append(input())
    # print(s)
    # print(t)
    # print(n)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == t[j] and t[i] == s[j]:
                return "Yes"
    return "No"
