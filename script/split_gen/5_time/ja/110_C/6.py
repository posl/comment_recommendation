def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    S_list = list(S)
    T_list = list(T)
    S_dict = {}
    T_dict = {}
    for i in range(S_len):
        if S_list[i] in S_dict:
            S_dict[S_list[i]] += 1
        else:
            S_dict[S_list[i]] = 1
    for i in range(T_len):
        if T_list[i] in T_dict:
            T_dict[T_list[i]] += 1
        else:
            T_dict[T_list[i]] = 1
    S_dict_sorted = sorted(S_dict.items(), key=lambda x:x[1], reverse=True)
    T_dict_sorted = sorted(T_dict.items(), key=lambda x:x[1], reverse=True)
    S_dict_sorted_len = len(S_dict_sorted)
    T_dict_sorted_len = len(T_dict_sorted)
    if S_dict_sorted_len != T_dict_sorted_len:
        print("No")
        exit()
    for i in range(S_dict_sorted_len):
        if S_dict_sorted[i][1] != T_dict_sorted[i][1]:
            print("No")
            exit()
    print("Yes")
