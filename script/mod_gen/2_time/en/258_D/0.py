def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A, B = zip(*sorted(zip(A, B)))
    if X == 1:
        print(A[0])
        return
    if X == 2:
        print(A[0]+B[0])
        return
    if N == 1:
        print(A[0]+B[0]*(X-1))
        return
    if N == 2:
        print(A[0]+min(A[0]+B[0]*(X-2), B[0]*(X-1)))
        return
    if X == N:
        print(sum(B))
        return
    if X == N+1:
        print(sum(B)+A[0])
        return
    if X == N+2:
        print(sum(B)+A[1])
        return
    if X == N+3:
        print(sum(B)+A[1]+B[0])
        return
    if X == N+4:
        print(sum(B)+A[1]+B[0]+B[1])
        return
    if X == N+5:
        print(sum(B)+A[1]+B[0]+B[1]+B[2])
        return
    if X == N+6:
        print(sum(B)+A[1]+B[0]+B[1]+B[2]+B[3])
        return
    if X == N+7:
        print(sum(B)+A[1]+B[0]+B[1]+B[2]+B[3]+B[4])
        return
    if X == N+8:
        print(sum(B)+A[1]+B[0]+B[1]+B[2]+B[3]+B[4]+B[5])
        return
    if X == N+9:
        print(sum(B)+A[1]+B[0]+B[1]+B[2]+B[3]+B[4]+B[5]+B[6])
        return
    if X == N+10:
        print(sum(B)+A[1]+B[0]+B[1]+B[2]+B[3]+

if __name__ == '__main__':
    main()