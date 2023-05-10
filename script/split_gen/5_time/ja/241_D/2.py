def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            if len(A) < query[2]:
                print(-1)
            else:
                print(sorted(A[:query[2]], reverse=True)[query[1]-1])
        elif query[0] == 3:
            if len(A) < query[2]:
                print(-1)
            else:
                print(sorted(A[query[2]-1:], reverse=False)[query[1]-1])
        else:
            print('Error')
