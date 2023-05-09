def main():
    A, B, C, K = map(int, input().split())
    print(min(A, K) - min(B, K - A) if K > A else min(A, K))
