def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, A, Q, BC)
    B = [0] * (10**5+1)
    for a in A:
        B[a] += 1
    S = sum(A)
    for b, c in BC:
        S += (c-b) * B[b]
        B[c] += B[b]
        B[b] = 0
        print(S)

if __name__ == '__main__':
    main()