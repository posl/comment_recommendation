def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > i + 1:
            continue
        for j in range(i + 1, N):
            if A[i] == j + 1 and A[j] == i + 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()