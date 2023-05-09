def main():
    N = int(input())
    A = []
    for i in range(N):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A = sorted(A)
            B = []
            for j in range(len(A)):
                if A[j] <= query[1]:
                    B.append(A[j])
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[-query[2]])
        else:
            A = sorted(A, reverse=True)
            B = []
            for j in range(len(A)):
                if A[j] >= query[1]:
                    B.append(A[j])
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[-query[2]])

if __name__ == '__main__':
    main()