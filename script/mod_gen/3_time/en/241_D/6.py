def main():
    # input
    Q = int(input())
    queries = [input().split() for _ in range(Q)]
    # compute
    A = []
    for query in queries:
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            cnt = 0
            for a in A:
                if a <= x:
                    cnt += 1
            if cnt < k:
                print(-1)
            else:
                A.sort(reverse=True)
                print(A[k-1])
        else:
            x = int(query[1])
            k = int(query[2])
            cnt = 0
            for a in A:
                if a >= x:
                    cnt += 1
            if cnt < k:
                print(-1)
            else:
                A.sort()
                print(A[k-1])

if __name__ == '__main__':
    main()