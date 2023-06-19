def main():
    # N,K = map(int,input().split())
    # A = []
    # for i in range(K):
    #     d = int(input())
    #     A.append(list(map(int,input().split())))
    N,K = 3,3
    A = [[1,3],[1],[3]]
    A = [sorted(a) for a in A]
    print(A)
    ans = 0
    for i in range(N):
        flag = 0
        for j in range(K):
            if i+1 in A[j]:
                flag = 1
        if flag == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()