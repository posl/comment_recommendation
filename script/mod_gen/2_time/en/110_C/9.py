def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    # Make a dictionary of characters in S and T
    S_dict = {}
    T_dict = {}
    for i in range(len(S)):
        if S[i] in S_dict:
            S_dict[S[i]].append(i)
        else:
            S_dict[S[i]] = [i]
        if T[i] in T_dict:
            T_dict[T[i]].append(i)
        else:
            T_dict[T[i]] = [i]
    # Check if the dictionary values are equal
    if sorted(S_dict.values()) == sorted(T_dict.values()):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()