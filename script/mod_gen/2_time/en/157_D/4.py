def main():
    N, M, K = map(int, input().split())
    friend = [[] for i in range(N)]
    block = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        friend[A - 1].append(B - 1)
        friend[B - 1].append(A - 1)
    for i in range(K):
        C, D = map(int, input().split())
        block[C - 1].append(D - 1)
        block[D - 1].append(C - 1)
    for i in range(N):
        friend[i].sort()
        block[i].sort()
    for i in range(N):
        cnt = 0
        for j in friend[i]:
            if i not in friend[j]:
                cnt += 1
        for j in block[i]:
            if i in friend[j]:
                cnt -= 1
        print(N - len(friend[i]) - cnt - 1, end = ' ')
    print()

if __name__ == '__main__':
    main()