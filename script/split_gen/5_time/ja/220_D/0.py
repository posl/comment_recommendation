def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    ans = [0] * 10
    ans[A[0]] = 1
    for i in range(1,N):
        ans2 = [0] * 10
        for j in range(10):
            ans2[(j+A[i]) % 10] += ans[j]
            ans2[(j*A[i]) % 10] += ans[j]
        ans = ans2
    for i in range(10):
        print(ans[i] % 998244353)
