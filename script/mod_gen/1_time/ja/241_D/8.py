def main():
    import sys
    input = sys.stdin.readline
    #入力
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #処理
    A = []
    for i in range(Q):
        if query[i][0] == 1:
            A.append(query[i][1])
        elif query[i][0] == 2:
            A.sort(reverse=True)
            for j in range(len(A)):
                if A[j] <= query[i][1]:
                    if j+1 == query[i][2]:
                        print(A[j])
                    elif j+1 > query[i][2]:
                        print(-1)
                    break
        elif query[i][0] == 3:
            A.sort()
            for j in range(len(A)):
                if A[j] >= query[i][1]:
                    if j+1 == query[i][2]:
                        print(A[j])
                    elif j+1 > query[i][2]:
                        print(-1)
                    break

if __name__ == '__main__':
    main()