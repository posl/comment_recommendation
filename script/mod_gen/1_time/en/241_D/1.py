def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort(reverse = True)
            count = 0
            for j in range(len(A)):
                if A[j] <= query[1]:
                    count += 1
                    if count == query[2]:
                        print(A[j])
                        break
            if count < query[2]:
                print(-1)
        else:
            A.sort()
            count = 0
            for j in range(len(A)):
                if A[j] >= query[1]:
                    count += 1
                    if count == query[2]:
                        print(A[j])
                        break
            if count < query[2]:
                print(-1)

if __name__ == '__main__':
    main()