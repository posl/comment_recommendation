def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    print(A.index(min(A[:2 ** (N - 1)])) + 1)
