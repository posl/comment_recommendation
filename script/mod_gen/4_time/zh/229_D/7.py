def solve():
    S = input()
    K = int(input())
    S = S.replace('.', ' ')
    S = S.split()
    ans = 0
    for s in S:
        ans += len(s) - K + 1 if len(s) - K + 1 > 0 else 0
    print(ans)

if __name__ == '__main__':
    solve()