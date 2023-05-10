def main():
    n = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(n):
        P += A[i]-1
        P = P%4
    print(P)
