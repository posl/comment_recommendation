def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
        for j in range(i + 1, i + N + 1):
            if ans[i] > T[j % N]:
                ans[i] = T[j % N] + S[j % N]
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()