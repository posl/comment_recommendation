def main():
    N, M, Q = [int(x) for x in input().split()]
    queries = []
    for _ in range(Q):
        queries.append([int(x) for x in input().split()])
    print(solve(N, M, Q, queries))
