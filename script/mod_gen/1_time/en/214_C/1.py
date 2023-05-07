def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
    for i in range(N):
        for j in range(i, i+N):
            if ans[j % N] > ans[(j+1) % N] + S[j % N]:
                ans[j % N] = ans[(j+1) % N] + S[j % N]
    for i in range(N):
        print(ans[i])
main()

if __name__ == '__main__':
    main()