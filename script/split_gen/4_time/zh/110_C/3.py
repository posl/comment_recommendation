def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    S_set = set(S)
    T_set = set(T)
    if S_set != T_set:
        print("No")
        return
    S_dic = {}
    T_dic = {}
    for i in range(len(S)):
        if S[i] in S_dic:
            S_dic[S[i]].append(i)
        else:
            S_dic[S[i]] = [i]
        if T[i] in T_dic:
            T_dic[T[i]].append(i)
        else:
            T_dic[T[i]] = [i]
    for key in S_dic:
        if S_dic[key] != T_dic[key]:
            print("No")
            return
    print("Yes")
    return
