def get_input():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        x, k = map(int, input().split())
        queries.append((x, k))
    return N, Q, A, queries

if __name__ == '__main__':
    get_input()