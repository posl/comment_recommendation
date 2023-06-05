def solve(N, S, T):
    if N == 2:
        if S[0] == S[1] or S[0] == T[1] or T[0] == S[1] or T[0] == T[1]:
            print("Yes")
        else:
            print("No")
    else:
        for i in range(N):
            for j in range(N):
                if i != j:
                    if S[i] == S[j] or S[i] == T[j] or T[i] == S[j] or T[i] == T[j]:
                        print("No")
                        return
        print("Yes")

if __name__ == '__main__':
    solve()