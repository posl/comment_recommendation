def solve():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == "w":
            ans += i
    print(ans)

if __name__ == '__main__':
    solve()