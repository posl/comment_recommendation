def main():
    N, K, X = map(int, input().split())
    A = map(int, input().split())
    total = 0
    for a in A:
        total += max(a - X, 0)
    print(total)
