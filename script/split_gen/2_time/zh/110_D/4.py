def solve():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        else:
            for j in range(i+1, len(S)):
                if S[j] == S[i]:
                    if T[j] == T[i]:
                        S = S[:i] + T[j] + S[i+1:]
                        T = T[:i] + S[j] + T[i+1:]
                        break
                    else:
                        print("No")
                        return
                elif T[j] == T[i]:
                    if S[j] == S[i]:
                        S = S[:i] + T[j] + S[i+1:]
                        T = T[:i] + S[j] + T[i+1:]
                        break
                    else:
                        print("No")
                        return
            if S[i] != T[i]:
                print("No")
                return
    print("Yes")
