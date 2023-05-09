def main():
    S = input()
    T = input()
    if len(S) == len(T):
        if S == T:
            print("Yes")
        else:
            print("No")
    else:
        for i in range(len(S)):
            if S[i] == T[i]:
                continue
            else:
                if S[i] == T[i+1] and S[i+1] == T[i]:
                    print("Yes")
                    break
                else:
                    print("No")
                    break

if __name__ == '__main__':
    main()