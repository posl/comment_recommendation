def main():
    N, Q = map(int, input().split())
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split())))
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    for i in range(Q):
        print(seq[queries[i][0]-1][queries[i][1]-1])
