def main():
    A, B, N = map(int, input().split())
    if N >= B-1:
        x = B-1
    else:
        x = N
    print(int(A*x/B) - A*int(x/B))
