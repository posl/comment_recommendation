def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            if len(A) < query[2]:
                print(-1)
            else:
                A.sort(reverse=True)
                print(A[query[2] - 1])
        elif query[0] == 3:
            if len(A) < query[2]:
                print(-1)
            else:
                A.sort()
                print(A[query[2] - 1])

if __name__ == '__main__':
    main()