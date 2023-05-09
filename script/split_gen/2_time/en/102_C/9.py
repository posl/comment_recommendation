def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #mid = A[N//2]
    mid = A[(N-1)//2]
    print(sum(abs(a-mid) for a in A))
