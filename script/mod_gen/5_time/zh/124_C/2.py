def solve():
    S = input()
    ans = 0
    for i in range(len(S)):
        if i % 2 == 0 and S[i] == '1':
            ans += 1
        elif i % 2 == 1 and S[i] == '0':
            ans += 1
    print(min(ans, len(S) - ans))

if __name__ == '__main__':
    solve()