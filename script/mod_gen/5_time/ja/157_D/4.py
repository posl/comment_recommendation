def main():
    N, M, K = map(int, input().split())
    friend = [[] for _ in range(N)]
    block = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friend[A - 1].append(B - 1)
        friend[B - 1].append(A - 1)
    for _ in range(K):
        C, D = map(int, input().split())
        block[C - 1].append(D - 1)
        block[D - 1].append(C - 1)
    for i in range(N):
        friend[i] = set(friend[i])
        block[i] = set(block[i])
    for i in range(N):
        print(len(friend[i] - block[i] - {i}) - 1, end=" ")
    print()

if __name__ == '__main__':
    main()