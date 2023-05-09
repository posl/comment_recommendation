def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    d = {}
    for q in range(Q):
        if query[q][0] == "1":
            d = {}
            d[int(query[q][1])] = N
        elif query[q][0] == "2":
            if int(query[q][2]) in d:
                d[int(query[q][2])] += 1
            else:
                d[int(query[q][2])] = 1
        else:
            if int(query[q][1]) in d:
                print(A[int(query[q][1]) - 1] + d[int(query[q][1])])
            else:
                print(A[int(query[q][1]) - 1])
