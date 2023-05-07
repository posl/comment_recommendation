def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P += 1
        else:
            P += 1
            P -= (A[i-1] + A[i]) // 4
    print(P)
