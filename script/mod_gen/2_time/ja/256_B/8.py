def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += 1
        P -= (A[i] + P) // 4
    print(P)
main()
