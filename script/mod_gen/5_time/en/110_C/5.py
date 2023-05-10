def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        for j in range(i+1, len(S)):
            if S[j] == T[i]:
                S = S[:i] + S[j] + S[i+1:j] + S[i] + S[j+1:]
                break
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()