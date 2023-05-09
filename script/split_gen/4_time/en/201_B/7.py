def main():
    N = int(input())
    A = [input().split() for _ in range(N)]
    A = sorted(A, key = lambda x: x[1], reverse=True)
    print(A[1][0])
