def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    ans = [0] * (N+1)
    for i in range(1, N+1):
        if K >= i:
            ans[i] = K // i
            K -= ans[i] * i
        else:
            ans[i] = 0
    for i in range(1, N+1):
        if K > 0:
            if a[i] <= K:
                ans[i] += 1
                K -= 1
            else:
                break
    for i in range(1, N+1):
        print(ans[i])

if __name__ == '__main__':
    main()