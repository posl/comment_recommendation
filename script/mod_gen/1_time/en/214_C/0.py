def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
        for j in range(i+1, N+i):
            if ans[i] > ans[j%N]:
                ans[j%N] = ans[i]
            else:
                ans[i] += S[j%N]
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()