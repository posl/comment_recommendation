def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if K * X >= sum(A):
        print(0)
    else:
        print(sum(A) - (K * X))
