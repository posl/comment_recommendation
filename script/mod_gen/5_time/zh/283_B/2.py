def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    # Q = int(input())
    # for _ in range(Q):
    #     query = list(map(int, input().split()))
    #     if query[0] == 1:
    #         A[query[1] - 1] = query[2]
    #     else:
    #         print(A[query[1] - 1])
    # 一行输入
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    for i in range(Q):
        if query[i][0] == 1:
            A[query[i][1] - 1] = query[i][2]
        else:
            print(A[query[i][1] - 1])

if __name__ == '__main__':
    main()