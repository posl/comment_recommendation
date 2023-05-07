def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            #print(A[i], A[j])
            ans = max(ans, abs(A[i]-A[j]))
    print(ans)
