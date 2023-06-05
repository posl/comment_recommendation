def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P = P - 1 if A[i] + i >= 4 else P
    print(P)
