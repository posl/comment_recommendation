def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    # N = 200000
    # A = [200000] * N
    # N = 2
    # A = [5, 5]
    B = sorted(A)
    maxA = B[-1]
    maxB = B[-2]
    for a in A:
        if a == maxA:
            print(maxB)
        else:
            print(maxA)
