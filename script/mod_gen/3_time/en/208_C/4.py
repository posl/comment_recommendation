def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a = sorted(a)
    ans = [0]*N
    for i in range(N):
        ans[i] = K//(N-i)
        K -= ans[i]
    for i in range(N):
        if K == 0:
            break
        ans[i] += 1
        K -= 1
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()