def main():
    N, T = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort(key=lambda x: x[0])
    ans = 1001
    for i in range(N):
        if A[i][1] <= T:
            ans = min(ans, A[i][0])
    if ans == 1001:
        print('TLE')
    else:
        print(ans)

if __name__ == '__main__':
    main()