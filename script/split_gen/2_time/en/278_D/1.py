def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    query = []
    for q in range(Q):
        query.append([int(x) for x in input().split()])
    add = [0] * N
    add_all = 0
    for q in range(Q):
        if query[q][0] == 1:
            add_all += query[q][1]
        elif query[q][0] == 2:
            add[query[q][1]-1] += query[q][2]
        else:
            print(A[query[q][1]-1] + add[query[q][1]-1] + add_all)
