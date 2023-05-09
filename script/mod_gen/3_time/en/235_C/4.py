def get_input():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = []
    for _ in range(q):
        x, k = map(int, input().split())
        queries.append((x, k))
    return n, q, a, queries

if __name__ == '__main__':
    get_input()