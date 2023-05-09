def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A = [L if a < L else R if a > R else a for a in A]
    print(sum(A))
