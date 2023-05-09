def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:N//2])+L*(N//2)+R*(N-N//2))
