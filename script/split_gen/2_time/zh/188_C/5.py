def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    print(A[N-2])
