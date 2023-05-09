def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if A[i] == 1:
            P += 1
        elif A[i] == 2:
            P += 2
        elif A[i] == 3:
            P += 3
        else:
            P += 4
    print(P)
