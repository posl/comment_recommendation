def main():
    N, M, K = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * K
    D = [0] * K
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    #print(N, M, K)
    #print(A)
    #print(B)
    #print(C)
    #print(D)
    #print()
    #print()
    #print()
    #朋友候选人数
    friend_candidate = [0] * N
    #友谊关系
    friendship = []
    #阻隔关系
    blockhip = []
    #初始朋友候选人数
    for i in range(N):
        friend_candidate[i] = N - 1
    #print(friend_candidate)
    #友谊关系
    for i in range(M):
        friendship.append([A[i], B[i]])
    #阻隔关系
    for i in range(K):
        blockhip.append([C[i], D[i]])
    #print(friendship)
    #print(blockhip)
    #初始朋友候选人数
    for i in range(N):
        for j in range(M):
            if friendship[j][0] == i + 1:
                friend_candidate[i] -= 1
            if friendship[j][1] == i + 1:
                friend_candidate[i] -= 1
        for j in range(K):
            if blockhip[j][0] == i + 1:
                friend_candidate[i] -= 1
            if blockhip[j][1] == i + 1:
                friend_candidate[i] -= 1
    #print(friend_candidate)
    #朋友候选人数
    for i in range(N):
        for j in range(M):
            if friendship[j][0] == i + 1:
                for k in range(N):
                    if friend_candidate[k] == 0:
                        continue
                    if friendship[j][1] == k + 1:
                        friend_candidate[k] -= 1
            if

if __name__ == '__main__':
    main()