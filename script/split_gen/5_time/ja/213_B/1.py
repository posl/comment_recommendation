def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    print(A.index(A_sorted[1]) + 1)
