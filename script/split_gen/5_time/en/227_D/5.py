def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    print(sum(A[:k]))
