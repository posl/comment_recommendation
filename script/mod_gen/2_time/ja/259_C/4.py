def main():
    S = list(input())
    T = list(input())
    if S == T:
        print("Yes")
        return
    if len(S) > len(T):
        print("No")
        return
    for i in range(len(S)):
        if S[i] != T[i]:
            if S[i] == T[i+1] and S[i+1] == T[i]:
                S[i], S[i+1] = S[i+1], S[i]
                if S == T:
                    print("Yes")
                    return
                else:
                    print("No")
                    return
            else:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()