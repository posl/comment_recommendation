def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = [[0, 0] for _ in range(N)]
    for i in range(N):
        ans[i][0] = H - A[i] + 1
        ans[i][1] = B[i]
    ans.sort()
    for i in range(N):
        print(ans[i][0], ans[i][1])

if __name__ == '__main__':
    main()