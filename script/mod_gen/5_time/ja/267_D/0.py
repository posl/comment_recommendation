def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        tmp = sum([j * A[i + j - 1] for j in range(1, M + 1)])
        if tmp > ans:
            ans = tmp
    print(ans)

if __name__ == '__main__':
    main()