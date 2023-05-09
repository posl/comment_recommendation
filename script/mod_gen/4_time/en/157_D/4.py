def main():
    N, M, K = map(int, input().split())
    friend = [0] * N
    block = [0] * N
    for i in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        friend[A] += 1
        friend[B] += 1
    for i in range(K):
        C, D = map(int, input().split())
        C -= 1
        D -= 1
        block[C] += 1
        block[D] += 1
    ans = [0] * N
    for i in range(N):
        ans[i] = friend[i] - block[i] - 1
    print(*ans)

if __name__ == '__main__':
    main()