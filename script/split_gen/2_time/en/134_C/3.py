def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    maxA2 = sorted(A)[-2]
    for a in A:
        if a == maxA:
            print(maxA2)
        else:
            print(maxA)
