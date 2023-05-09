def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                ans ^= A[i][j]
    print(ans)

if __name__ == '__main__':
    main()