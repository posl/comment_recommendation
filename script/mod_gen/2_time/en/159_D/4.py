def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0 for _ in range(N+1)]
    for a in A:
        cnt[a] += 1
    ans = [0 for _ in range(N)]
    for i in range(N):
        ans[i] = sum(cnt) - cnt[A[i]]
    for a in ans:
        print(a//2)

if __name__ == '__main__':
    main()