def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P += 1
        else:
            if A[i-1] == 1:
                P += 1
            elif A[i-1] == 2:
                P += 2
            elif A[i-1] == 3:
                P += 3
            elif A[i-1] == 4:
                P += 4
            else:
                pass
    print(P)
