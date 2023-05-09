def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if A[N - i - 1] == 1:
            ans.append(N - i)
            for j in range(2, (N - i) // 2 + 1):
                if (N - i) % j == 0:
                    A[j - 1] = (A[j - 1] + 1) % 2
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()