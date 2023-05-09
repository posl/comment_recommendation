def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    #solve
    ans = [0] * Q
    B = [0] * (10**5+1)
    for a in A:
        B[a] += 1
    S = sum(A)
    for i in range(Q):
        b, c = BC[i]
        S -= B[b] * b
        S += B[b] * c
        B[c] += B[b]
        B[b] = 0
        ans[i] = S
    #output
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()