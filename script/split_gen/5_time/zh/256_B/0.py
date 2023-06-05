def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    P = 0
    for i in range(N):
        P += A[i] - 1
        P %= 4
    print(P)
