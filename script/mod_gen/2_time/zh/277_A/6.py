def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                print(cnt)
                return
        cnt += 1
        if cnt > 100:
            print(-1)
            return

if __name__ == '__main__':
    solve()