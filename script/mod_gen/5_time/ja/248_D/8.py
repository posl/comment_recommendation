def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for i in range(Q):
        L = Query[i][0] - 1
        R = Query[i][1] - 1
        X = Query[i][2]
        cnt = 0
        for j in range(L, R+1):
            if A[j] == X:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()