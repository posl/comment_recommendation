def solve():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            ans += 1
    print(ans)
    return 0

if __name__ == '__main__':
    solve()