def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(int(A*N/B))
    else:
        print(int(A*(B-1)/B))
