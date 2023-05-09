def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A = sorted([(A[i], i) for i in range(N)])
    B = sorted([(B[i], i) for i in range(N)])
    ans = [[0, 0] for _ in range(N)]
    i = 0
    for a, idx in A:
        ans[idx][0] = i + 1
        i += 1
        while i < N and A[i][0] == a:
            ans[A[i][1]][0] = i + 1
            i += 1
    i = 0
    for b, idx in B:
        ans[idx][1] = i + 1
        i += 1
        while i < N and B[i][0] == b:
            ans[B[i][1]][1] = i + 1
            i += 1
    for i in range(N):
        print(*ans[i])

if __name__ == '__main__':
    main()