def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    ans = [0] * N
    for i in range(N):
        ans[i] = K // N
        if i < K % N:
            ans[i] += 1
    #print(ans)
    for i in range(N):
        if a[i] <= K:
            print(ans[i])
        else:
            print(0)

if __name__ == '__main__':
    main()