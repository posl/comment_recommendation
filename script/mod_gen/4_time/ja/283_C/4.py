def solve():
    S = input()
    ans = 0
    while len(S) > 1:
        if S[-1] == "0":
            S = S[:-1]
        else:
            S = str(int(S) - 1)
        ans += 1
    print(ans + int(S))

if __name__ == '__main__':
    solve()