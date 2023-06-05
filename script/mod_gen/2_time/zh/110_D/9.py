def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    # Sの各文字の出現回数を数える
    S_count = {}
    for c in S:
        if c in S_count:
            S_count[c] += 1
        else:
            S_count[c] = 1
    # Tの各文字の出現回数を数える
    T_count = {}
    for c in T:
        if c in T_count:
            T_count[c] += 1
        else:
            T_count[c] = 1
    # Sの各文字の出現回数とTの各文字の出現回数が一致するかどうかを調べる
    for c in S_count.keys():
        if c not in T_count.keys():
            print("No")
            return
        if S_count[c] != T_count[c]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()