def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    P = 0
    for i in range(N):
        P += 1
        P += (i + A[i]) // 4
    print(P)
