def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if i == 0:
            ans[i] = 1
            cnt = 1
        else:
            if A[i] != A[i-1]:
                ans[i] = cnt
                cnt = 1
            else:
                cnt += 1
    ans[N-1] = cnt
    ans = ans[::-1]
    ans2 = [0] * N
    ans2[0] = ans[0]
    for i in range(1, N):
        ans2[i] = ans2[i-1] + ans[i]
    ans2 = ans2[::-1]
    for i in range(N):
        print(ans2[i])

if __name__ == '__main__':
    main()