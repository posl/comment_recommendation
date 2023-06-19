def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        x = A[i] - 1
        P += x
    print(P)
