def main():
    N = int(input())
    A = list(map(int,input().split()))
    P = 0
    for i in range(N):
        P += 1
        if A[i] >= 4:
            P += 1
    print(P)
