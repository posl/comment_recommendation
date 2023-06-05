def main():
    S = input()
    T = input()
    S_dict = {}
    T_dict = {}
    for i in range(len(S)):
        if S[i] not in S_dict.keys():
            S_dict[S[i]] = T[i]
        else:
            if S_dict[S[i]] != T[i]:
                print("No")
                return
        if T[i] not in T_dict.keys():
            T_dict[T[i]] = S[i]
        else:
            if T_dict[T[i]] != S[i]:
                print("No")
                return
    print("Yes")
