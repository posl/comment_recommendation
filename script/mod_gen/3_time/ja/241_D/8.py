def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    A = []
    D = defaultdict(int)
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
            D[query[1]] += 1
        elif query[0] == 2:
            A.sort()
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[query[2]-1])
        else:
            A.sort(reverse = True)
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[query[2]-1])

if __name__ == '__main__':
    main()