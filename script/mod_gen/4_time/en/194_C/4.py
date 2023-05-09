def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += sum([(A[i] - A[j])**2 for j in range(i)])
    print(ans)

if __name__ == '__main__':
    solve()