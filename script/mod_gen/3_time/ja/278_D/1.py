def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int,input().split())))
    for i in range(Q):
        if query[i][0] == 1:
            A = [query[i][1]]*N
        elif query[i][0] == 2:
            A[query[i][1]-1] += query[i][2]
        else:
            print(A[query[i][1]-1])

if __name__ == '__main__':
    main()