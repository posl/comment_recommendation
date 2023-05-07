def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(len(A)):
        if i == 0:
            P += 1
        else:
            P += A[i-1]
        if P >= 4:
            P -= 4
    print(P)
