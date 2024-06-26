def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            if query[1] in A:
                A.sort()
                print(A[-query[2]] if len(A) >= query[2] else -1)
            else:
                print(-1)
        elif query[0] == 3:
            if query[1] in A:
                A.sort()
                print(A[query[2]-1] if len(A) >= query[2] else -1)
            else:
                print(-1)
        else:
            print("error")
    return

if __name__ == '__main__':
    main()