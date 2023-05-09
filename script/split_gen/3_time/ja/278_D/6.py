def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    sumA = sum(A)
    for query in queries:
        if query[0] == 1:
            sumA = sumA - N*query[1]
        elif query[0] == 2:
            sumA = sumA + query[1]*A[query[2]-1]
            A[query[2]-1] = A[query[2]-1] + query[1]
        else:
            print(A[query[1]-1])
main()
