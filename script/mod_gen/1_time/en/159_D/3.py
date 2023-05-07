def main():
    N = int(input())
    A = list(map(int,input().split()))
    cnt = [0] * (N+1)
    for i in range(N):
        cnt[A[i]] += 1
    ans = [0] * (N+1)
    for i in range(1,N+1):
        ans[i] = cnt[i]*(cnt[i]-1)//2
    total = sum(ans)
    for i in range(N):
        print(total-ans[A[i]]+1)

if __name__ == '__main__':
    main()