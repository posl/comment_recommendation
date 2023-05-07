def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(N * max(A) - sum(A))
