def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    if A[0] == 1:
        print(1)
        return
    else:
        GCD = A[0]
        for i in range(1,N):
            GCD = gcd(GCD,A[i])
        print(GCD)
