def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    cnt = 1
    ans = []
    for i in range(N):
        if A[i] == A[i+1]:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
    ans.append(0)
    ans.append(0)
    for i in range(1, N+1):
        ans[N-i] += ans[N-i+1]
        print(ans[N-i] - ans[i+1])

if __name__ == '__main__':
    main()