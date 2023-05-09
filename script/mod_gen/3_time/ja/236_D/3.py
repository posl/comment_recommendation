def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans ^= A[i][i + 1]
    print(ans)

if __name__ == '__main__':
    main()