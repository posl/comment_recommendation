def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j])**2
    print(ans)
