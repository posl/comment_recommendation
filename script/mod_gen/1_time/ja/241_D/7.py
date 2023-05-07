def main():
    #入力
    Q = int(input())
    A = []
    for q in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            A = list(set(A))
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[query[2]-1])
        elif query[0] == 3:
            A.sort(reverse=True)
            A = list(set(A))
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[query[2]-1])

if __name__ == '__main__':
    main()