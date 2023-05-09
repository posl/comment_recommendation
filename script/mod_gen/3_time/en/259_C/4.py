def main():
    S = input()
    T = input()
    if len(S) == len(T):
        if S == T:
            print("Yes")
        else:
            print("No")
    else:
        if len(T) - len(S) == 1:
            for i in range(len(S)):
                if S[i] == T[i]:
                    continue
                else:
                    if S[i:] == T[i+1:]:
                        print("Yes")
                    else:
                        print("No")
                    break
        else:
            print("No")

if __name__ == '__main__':
    main()