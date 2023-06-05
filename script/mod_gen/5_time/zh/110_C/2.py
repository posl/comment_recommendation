def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    S_dict = {}
    T_dict = {}
    for i in range(len(S)):
        if S[i] not in S_dict:
            S_dict[S[i]] = []
        S_dict[S[i]].append(i)
        if T[i] not in T_dict:
            T_dict[T[i]] = []
        T_dict[T[i]].append(i)
    for key in S_dict:
        if key not in T_dict:
            print("No")
            return
        if len(S_dict[key]) != len(T_dict[key]):
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()