def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    edges = [(a-1, b-1) for a, b in edges]
    print(count_ways(n, edges))
