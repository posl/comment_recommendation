def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print("N = ", N)
    #print("A = ", A)
    ans = 0
    cnt = [0] * (N + 1)
    for i in range(N):
        cnt[A[i]] += 1
    #print("cnt = ", cnt)
    for i in range(1, N + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2
    #print("ans = ", ans)
    for i in range(N):
        print(ans - (cnt[A[i]] - 1))
    return

if __name__ == '__main__':
    main()