def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 2 ** 30
    for i in range(N):
        x = 0
        for j in range(i, N):
            x = x | A[j]
            y = 0
            for k in range(j + 1, N):
                y = y ^ A[k]
            ans = min(ans, x + y)
    print(ans)
main()
