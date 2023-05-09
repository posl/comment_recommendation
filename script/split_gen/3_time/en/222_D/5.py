def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(A[i], B[i] + 1):
            dp[i + 1] += dp[i]
            dp[i + 1] %= mod
    print(dp[N])
main()
I have a question regarding the following question.
https://atcoder.jp/contests/abc172/tasks/abc172_e
I have tried to solve it using the following code, but it got TLE. Can you please tell me the reason for the TLE?
I am a beginner in programming and I am not able to understand the reason for TLE.
import math
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
b=list(map(int,input().split()))
b.sort()
ans=math.inf
for i in range(n):
    for j in range(m):
        ans=min(ans,abs(a[i]-b[j]))
print(ans)
I have a problem with the code below. I am trying to print the sum of the products of the elements of the two arrays. The problem is that the output is not the sum of the products of the elements of the two arrays. I think the problem is in the for loop. I think I need to use a while loop. Can you help me?
