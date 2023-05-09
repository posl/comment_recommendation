def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    T = [(T[i], i + 1) for i in range(N)]
    T.sort()
    T = [0] + [T[i][1] for i in range(N)]
    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        if ans[i] == 0:
            ans[i] = T[i]
            j = T[i]
            while ans[j] == 0:
                ans[j] = T[i]
                j = T[j]
    for i in range(1, N + 1):
        print(ans[i])

if __name__ == '__main__':
    main()