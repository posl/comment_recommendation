def solve():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    if S_len != T_len:
        print("No")
        return
    S_list = list(S)
    T_list = list(T)
    if S_list == T_list:
        print("Yes")
        return
    S_list.sort()
    T_list.sort()
    if S_list != T_list:
        print("No")
        return
    S_list.sort()
    T_list.sort()
    S_dict = {}
    T_dict = {}
    for i in range(S_len):
        if S_list[i] not in S_dict:
            S_dict[S_list[i]] = 1
        else:
            S_dict[S_list[i]] += 1
        if T_list[i] not in T_dict:
            T_dict[T_list[i]] = 1
        else:
            T_dict[T_list[i]] += 1
    for i in range(S_len):
        if S_dict[S_list[i]] != T_dict[T_list[i]]:
            print("No")
            return
    print("Yes")
    return
