def main():
    N, M, K = map(int, input().split())
    friend_list = [[] for _ in range(N)]
    block_list = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friend_list[A-1].append(B-1)
        friend_list[B-1].append(A-1)
    for _ in range(K):
        C, D = map(int, input().split())
        block_list[C-1].append(D-1)
        block_list[D-1].append(C-1)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(friend_list[i]) - 1
        for j in friend_list[i]:
            if i in block_list[j]:
                ans[i] -= 1
    print(*ans)

if __name__ == '__main__':
    main()