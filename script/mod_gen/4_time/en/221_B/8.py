def solve():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[i] != T[i]:
            if S[i+1] == T[i] and S[i] == T[i+1]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    solve()