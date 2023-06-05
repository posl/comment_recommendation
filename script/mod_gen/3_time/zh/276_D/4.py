def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        odd = False
        for i in range(N):
            if A[i] % 2 != 0:
                odd = True
        if odd:
            break
        for i in range(N):
            A[i] = A[i] // 2
        ans += 1
    print(ans)

if __name__ == '__main__':
    solve()