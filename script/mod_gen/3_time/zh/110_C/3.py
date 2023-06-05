def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    if len(S) != len(T):
        print("No")
        return
    else:
        for i in range(len(S)):
            if S[i] == T[i]:
                continue
            else:
                #print(S[i])
                #print(T[i])
                #print(S.find(T[i]))
                #print(T.find(S[i]))
                if S.find(T[i]) != -1 and T.find(S[i]) != -1:
                    if S[i] == T[S.find(T[i])] and T[i] == S[T.find(S[i])]:
                        continue
                    else:
                        print("No")
                        return
                else:
                    print("No")
                    return
        print("Yes")
        return

if __name__ == '__main__':
    main()