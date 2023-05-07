def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    for i in range(Q):
        query = [int(x) for x in input().split()]
        if len(query) == 2:
            print(A[query[1] - 1])
        else:
            A[query[1] - 1] = query[2]

if __name__ == '__main__':
    main()