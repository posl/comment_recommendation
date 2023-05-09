def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if a[N - i - 1] == 1:
            if sum(a[N - i - 1::N - i]) % 2 == 0:
                ans.append(N - i)
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()