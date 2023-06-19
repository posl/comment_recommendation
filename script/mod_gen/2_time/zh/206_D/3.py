def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A + [0]
    c = {}
    for i in range(N + 2):
        if A[i] not in c:
            c[A[i]] = 1
        else:
            c[A[i]] += 1
    ans = 0
    for i in c:
        ans += c[i] // 2
    print(ans)

if __name__ == '__main__':
    solve()