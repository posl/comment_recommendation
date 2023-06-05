def main():
    n, q = map(int, input().split())
    roads = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        roads.append((a, b))
    queries = []
    for _ in range(q):
        c, d = map(int, input().split())
        queries.append((c, d))
    for c, d in queries:
        if (c, d) in roads or (d, c) in roads:
            print("Road")
        else:
            print("Town")
