def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i]
        if P >= 4:
            P -= 4
    print(P)
