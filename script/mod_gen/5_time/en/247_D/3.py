def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[2])
        else:
            print(sum(A[:query[1]]))
            A = A[query[1]:]

if __name__ == '__main__':
    main()