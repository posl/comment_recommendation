def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            if query[1] >= A[-1]:
                print(-1)
            else:
                for i in range(len(A)):
                    if A[i] > query[1]:
                        if len(A[i:]) >= query[2]:
                            print(A[i+query[2]-1])
                        else:
                            print(-1)
                        break
        else:
            A.sort(reverse=True)
            if query[1] <= A[-1]:
                print(-1)
            else:
                for i in range(len(A)):
                    if A[i] < query[1]:
                        if len(A[i:]) >= query[2]:
                            print(A[i+query[2]-1])
                        else:
                            print(-1)
                        break

if __name__ == '__main__':
    main()