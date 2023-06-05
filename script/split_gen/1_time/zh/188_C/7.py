def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    print(A.index(B[-2]) + 1)
