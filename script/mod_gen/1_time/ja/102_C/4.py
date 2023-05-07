def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10 ** 9
    for b in range(-100, 101):
        tmp = 0
        for i in range(N):
            tmp += abs(A[i] - (b + i + 1))
        ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()