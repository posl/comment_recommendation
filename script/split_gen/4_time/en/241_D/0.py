def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[-query[2]])
        else:
            A.sort()
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[query[2]-1])
