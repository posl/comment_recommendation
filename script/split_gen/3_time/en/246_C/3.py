def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    B = [max(a - X * K, 0) for a in A]
    print(sum(B))
