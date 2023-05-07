def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # sort by price
    idx = sorted(range(N), key=lambda k: A[k])
    A = [A[i] for i in idx]
    B = [B[i] for i in idx]
    ans = 0
    for i in range(N):
        if B[i] >= M:
            ans += A[i] * M
            break
        else:
            ans += A[i] * B[i]
            M -= B[i]
    print(ans)

if __name__ == '__main__':
    main()