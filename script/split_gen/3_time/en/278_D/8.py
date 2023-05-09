def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(str, input().split())) for _ in range(Q)]
    # 1, 2, 3のクエリをそれぞれ分けて保持する
    queries_1 = []
    queries_2 = []
    queries_3 = []
    for query in queries:
        if query[0] == "1":
            queries_1.append(query)
        elif query[0] == "2":
            queries_2.append(query)
        else:
            queries_3.append(query)
    # 1のクエリを処理する
    for query in queries_1:
        A = [int(query[1])] * N
    # 2のクエリを処理する
    for query in queries_2:
        A[int(query[1]) - 1] += int(query[2])
    # 3のクエリを処理する
    for query in queries_3:
        print(A[int(query[1]) - 1])
