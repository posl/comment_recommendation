def main():
    N = int(input())
    A = []
    for _ in range(N):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A = sorted(A)
            if len(A) >= query[2]:
                print(A[-query[2]])
            else:
                print(-1)
        elif query[0] == 3:
            A = sorted(A)
            if len(A) >= query[2]:
                print(A[query[2]-1])
            else:
                print(-1)

if __name__ == '__main__':
    main()