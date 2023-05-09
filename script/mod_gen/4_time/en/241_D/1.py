def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            cnt = 0
            for i in range(len(A)):
                if A[i] <= query[1]:
                    cnt += 1
                    if cnt == query[2]:
                        print(A[i])
                        break
            if cnt < query[2]:
                print(-1)
        else:
            A.sort(reverse=True)
            cnt = 0
            for i in range(len(A)):
                if A[i] >= query[1]:
                    cnt += 1
                    if cnt == query[2]:
                        print(A[i])
                        break
            if cnt < query[2]:
                print(-1)

if __name__ == '__main__':
    main()