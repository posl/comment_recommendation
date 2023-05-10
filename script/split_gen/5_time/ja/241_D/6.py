def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort(reverse=True)
            if query[1] not in A:
                print(-1)
            else:
                print(A.index(query[1])+1)
        elif query[0] == 3:
            A.sort()
            if query[1] not in A:
                print(-1)
            else:
                print(A.index(query[1])+1)
        else:
            print('error')
