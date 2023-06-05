def solve():
    N = int(input())
    A = []
    for i in range(N):
        L = list(map(int, input().split()))
        A.append(L[1:])
    A.sort()
    ans = 0
    prev = None
    for i in range(N):
        if A[i] != prev:
            ans += 1
            prev = A[i]
    print(ans)

if __name__ == '__main__':
    solve()