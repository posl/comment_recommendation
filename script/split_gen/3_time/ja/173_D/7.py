def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    ans = 0
    for i in range(N):
        #print(i)
        #print(A[i])
        #print(A[i] * (N - i - 1))
        ans += A[i] * (N - i - 1)
    print(ans)
