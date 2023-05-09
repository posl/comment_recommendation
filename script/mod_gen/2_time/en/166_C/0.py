def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, M)
    #print(H)
    #print(A)
    #print(B)
    good = [True] * N
    for i in range(M):
        if H[A[i]-1] <= H[B[i]-1]:
            good[A[i]-1] = False
        if H[B[i]-1] <= H[A[i]-1]:
            good[B[i]-1] = False
    print(sum(good))
main()
I think this is a good way to solve this problem.
I tried to solve this problem with the following code.
But it is too slow.

if __name__ == '__main__':
    main()