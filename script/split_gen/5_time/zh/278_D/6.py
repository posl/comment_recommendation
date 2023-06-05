def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    queries.reverse()
    for query in queries:
        if query[0] == 1:
            A = list(map(lambda x: query[1], A))
        elif query[0] == 2:
            A[query[1] - 1] += query[2]
        else:
            print(A[query[1] - 1])
