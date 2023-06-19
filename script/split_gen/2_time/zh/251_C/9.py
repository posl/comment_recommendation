def problems251_c():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    # print(S)
    # print(T)
    # S = ['bb', 'ba', 'aa', 'bb', 'ba', 'aa', 'aa', 'ab', 'bb', 'ab']
    # T = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    # N = len(S)
    # 按照T的降序排序
    T_sort = sorted(T, reverse=True)
    # print(T_sort)
    # 按照T的降序排序后，如果有相同的T值，那么按照S的升序排序
    T_sort_S = []
    for i in range(len(T_sort)):
        T_sort_S.append([T_sort[i], S[T.index(T_sort[i])]])
    # print(T_sort_S)
    # 按照T的降序排序后，如果有相同的T值，那么按照S的升序排序后，再按照S的升序排序
    T_sort_S_S = sorted(T_sort_S, key=lambda x: x[1])
    # print(T_sort_S_S)
    # 按照T的降序排序后，如果有相同的T值，那么按照S的升序排序后，再按照S的升序排序后，再按照T的降序排序
    T_sort_S_S_T = sorted(T_sort_S_S, key=lambda x: x[0], reverse=True)
    # print(T_sort_S_S_T)
    # 按照T的降序排序后，如果有相同的T值，那么按照S的升序排序后，再按照S的升序排序后，再按照T的降序排序后，再按照T的升序排序
    T_sort_S_S_T_T = sorted(T_sort_S_S_T, key=lambda x: x[0])
