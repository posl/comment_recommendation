def main():
    S = input()
    T = input()
    if len(S) == len(T) and len(S) >= 2 and len(S) <= 100 and len(T) >= 2 and len(T) <= 100:
        if S == T:
            print("Yes")
        else:
            S = list(S)
            T = list(T)
            for i in range(len(S)):
                for j in range(i+1, len(S)):
                    S[i], S[j] = S[j], S[i]
                    if S == T:
                        print("Yes")
                        break
                    else:
                        S = list(S)
                if S == T:
                    break
            if S != T:
                print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()