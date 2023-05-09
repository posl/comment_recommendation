def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    for i in range(N):
        if K > (N - 1 - i):
            ans[i] += K // (N - i)
            K = K % (N - i)
        else:
            ans[i] += K
            break
    for i in range(N):
        print(ans[i] + (a[i] - 1))

if __name__ == '__main__':
    main()