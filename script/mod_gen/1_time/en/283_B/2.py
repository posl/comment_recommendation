def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        elif query[0] == 2:
            print(A[query[1]-1])
        else:
            pass

if __name__ == '__main__':
    main()