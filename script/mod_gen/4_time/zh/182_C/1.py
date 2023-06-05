def solve():
    N = int(input())
    K = len(str(N))
    if N % 3 == 0:
        print(0)
        return
    for i in range(K):
        for j in range(10):
            if (N - j) % 3 == 0:
                print(i + 1)
                return
        N //= 10
    print(-1)

if __name__ == '__main__':
    solve()