def main():
    N, K = input().split()
    N = int(N)
    K = int(K)
    A = input().split()
    B = input().split()
    A = [int(s) for s in A]
    B = [int(s) for s in B]
    A.sort(reverse=True)
    B.sort()
    for i in range(K):
        for j in range(N):
            if B[i] == j+1:
                A[j] = 0
    if max(A) == 0:
        print("No")
    else:
        print("Yes")
main()
