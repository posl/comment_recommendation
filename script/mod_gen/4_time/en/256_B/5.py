def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    S = [0] * 4
    for i in range(N):
        S[A[i]-1] += 1
    for i in range(4):
        if S[i] > 0:
            P += 1
    print(P)

if __name__ == '__main__':
    main()