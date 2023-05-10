def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A + [0]
    #print(A)
    cnt = {}
    for i in range(1, N+1):
        if A[i] in cnt:
            cnt[A[i]] += 1
        else:
            cnt[A[i]] = 1
    #print(cnt)
    ans = 0
    for i in range(1, N+1):
        ans += cnt[A[i]] - 1
    for i in range(1, N+1):
        print(ans - cnt[A[i]] + 1)

if __name__ == '__main__':
    main()