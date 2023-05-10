def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
    for i in range(N):
        if i == N - 1:
            if ans[i] + S[i] < ans[0]:
                ans[0] = ans[i] + S[i]
        else:
            if ans[i] + S[i] < ans[i + 1]:
                ans[i + 1] = ans[i] + S[i]
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()