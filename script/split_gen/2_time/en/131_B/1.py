def main():
    N, L = map(int, input().split())
    A = [L + i - 1 for i in range(1, N + 1)]
    print(sum(A) - min(A, key=abs))
