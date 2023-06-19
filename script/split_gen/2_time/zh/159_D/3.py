def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*(N+1)
    count = 0
    for i in range(N):
        B[A[i]] += 1
    for i in range(N):
        count += B[i]*(B[i]-1)/2
    for i in range(N):
        print(int(count-(B[A[i]]-1)))
