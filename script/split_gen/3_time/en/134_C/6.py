def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    for a in A:
        if a == maxA:
            maxA2 = max(A)
        else:
            maxA2 = maxA
        print(maxA2)
