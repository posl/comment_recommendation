def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    S = [0] * Q
    S[0] = sum(A)
    for i in range(1, Q):
        S[i] = S[i-1] + (C[i] - B[i]) * A.count(B[i])
    for i in range(Q):
        print(S[i])

if __name__ == '__main__':
    main()