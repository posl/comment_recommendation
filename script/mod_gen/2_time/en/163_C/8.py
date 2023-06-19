def main():
    N = int(input())
    A = list(map(int,input().split()))
    if N == 2:
        print(1)
        print(0)
        return
    A.append(0)
    B = [0] * (N+1)
    for i in range(N):
        B[A[i]] += 1
    for i in range(1,N+1):
        print(B[i])
main()
