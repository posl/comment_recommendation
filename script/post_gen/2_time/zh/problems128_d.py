Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    V = list(map(int,input().split()))
    max_sum = 0
    for i in range(0,min(N,K)+1):
        for j in range(0,min(N,K)-i+1):
            left = V[:i]
            right = V[N-j:]
            if len(left) > 0:
                left.sort()
                for k in range(0,min(len(left),K-i-j)):
                    if left[k] < 0:
                        left[k] = 0
                    else:
                        break
            if len(right) > 0:
                right.sort(reverse=True)
                for k in range(0,min(len(right),K-i-j)):
                    if right[k] < 0:
                        right[k] = 0
                    else:
                        break
            if len(left) > 0:
                left.sort(reverse=True)
                max_sum = max(max_sum,sum(left[:K-i-j])+sum(right[:K-i-j]))
            else:
                max_sum = max(max_sum,sum(right[:K-i-j]))
    print(max_sum)

=======
Suggestion 2

def max_jewel_value(n, k, v):
    max_v = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) + 1 - i):
            v2 = v[:i] + v[-j:]
            v2.sort()
            max_v = max(max_v, sum(v2))
    return max_v

=======
Suggestion 3

def solve(n,k,nums):
    dp = [[[-float('inf') for i in range(2)] for j in range(k+1)] for k in range(n+1)]
    dp[0][0][0] = 0
    dp[0][0][1] = 0
    for i in range(n):
        for j in range(k+1):
            dp[i+1][j][0] = max(dp[i+1][j][0],dp[i][j][0])
            dp[i+1][j][1] = max(dp[i+1][j][1],dp[i][j][1])
            if j < k:
                dp[i+1][j+1][1] = max(dp[i+1][j+1][1],dp[i][j][0]+nums[i])
                dp[i+1][j+1][0] = max(dp[i+1][j+1][0],dp[i][j][1]-nums[i])
    return max(dp[n][k][0],dp[n][k][1])

n,k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
print(solve(n,k,nums))

=======
Suggestion 4

def solve():
    n,k = map(int,input().split())
    v = list(map(int,input().split()))
    ans = 0
    for i in range(min(n,k)+1):
        for j in range(min(n,k)-i+1):
            a = v[:i]
            b = v[n-j:]
            c = a + b
            c.sort()
            ans = max(ans,sum(c[max(0,k-i-j):]))
    print(ans)

solve()

=======
Suggestion 5

def get_max_value(N, K, V):
    max_value = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i+j <= N and i+j <= K:
                temp = 0
                for k in range(i):
                    temp += V[k]
                for k in range(N-j, N):
                    temp += V[k]
                if temp > max_value:
                    max_value = temp
    return max_value

=======
Suggestion 6

def solve(N,K,V):
    ans = 0
    for l in range(min(N,K)+1):
        for r in range(min(N,K)-l+1):
            s = 0
            t = []
            for i in range(l):
                s += V[i]
                t.append(V[i])
            for i in range(r):
                s += V[N-1-i]
                t.append(V[N-1-i])
            t.sort()
            for i in range(min(K-l-r,l+r)):
                if t[i] < 0:
                    s -= t[i]
            ans = max(ans,s)
    return ans

N,K = map(int,input().split())
V = list(map(int,input().split()))
print(solve(N,K,V))

=======
Suggestion 7

def max_sum(n,k,v):
    if n == k:
        return sum(v)
    if k == 0:
        return 0
    if n == 1:
        return max(v[0],0)
    if k == 1:
        return max(v[0],v[-1],0)
    if n == 2:
        return max(v[0]+v[1],v[0],v[1],0)
    if k == 2:
        return max(v[0]+v[1],v[0]+v[-1],v[-1]+v[-2],v[0],v[1],v[-1],v[-2],0)
    if n == 3:
        return max(v[0]+v[1]+v[2],v[0]+v[1],v[0]+v[2],v[1]+v[2],v[0],v[1],v[2],0)
    if k == 3:
        return max(v[0]+v[1]+v[2],v[0]+v[1]+v[-1],v[0]+v[-2]+v[-1],v[-3]+v[-2]+v[-1],v[0]+v[1],v[0]+v[2],v[1]+v[2],v[0]+v[-1],v[-1]+v[-2],v[-2]+v[-3],v[0],v[1],v[2],v[-1],v[-2],v[-3],0)
    if n == 4:
        return max(v[0]+v[1]+v[2]+v[3],v[0]+v[1]+v[2],v[0]+v[1]+v[3],v[0]+v[2]+v[3],v[1]+v[2]+v[3],v[0]+v[1],v[0]+v[2],v[0]+v[3],v[1]+v[2],v[1]+v[3],v[2]+v[3],v[0],v[1],v[2],v[3],0)
    if k == 4:
        return max(v[0]+v[1]+v[2]+v

=======
Suggestion 8

def input():
    N,K = map(int,raw_input().split())
    V = map(int,raw_input().split())
    return N,K,V

=======
Suggestion 9

def f(n,k,vs):
    if k==0:
        return 0
    if n==0:
        return 0
    if n==1:
        return vs[0]
    if n==2:
        return max(vs[0],vs[1])
    if n==3:
        return max(vs[0],vs[1],vs[2])
    if n==4:
        return max(vs[0]+vs[3],vs[1]+vs[2])
    if n==5:
        return max(vs[0]+vs[3],vs[1]+vs[2],vs[0]+vs[4],vs[1]+vs[3],vs[2]+vs[3],vs[3]+vs[4])
    if n==6:
        return max(vs[0]+vs[3]+vs[5],vs[1]+vs[2]+vs[4],vs[0]+vs[4]+vs[5],vs[0]+vs[1]+vs[3],vs[1]+vs[2]+vs[3],vs[2]+vs[3]+vs[4],vs[3]+vs[4]+vs[5])
    if n==7:
        return max(vs[0]+vs[3]+vs[5],vs[1]+vs[2]+vs[4],vs[0]+vs[4]+vs[5],vs[0]+vs[1]+vs[3]+vs[6],vs[1]+vs[2]+vs[3]+vs[5],vs[2]+vs[3]+vs[4]+vs[6],vs[3]+vs[4]+vs[5]+vs[6],vs[0]+vs[3]+vs[4]+vs[6],vs[1]+vs[2]+vs[5]+vs[6],vs[2]+vs[4]+vs[5]+vs[6],vs[0]+vs[1]+vs[2]+vs[3],vs[1]+vs[2]+vs[3]+vs[4],vs[2]+vs[3]+vs[4]+vs[5],vs[3]+vs[4]+vs[5]+vs[6])
    if n==8:
        return max(vs[0]+vs[3]+vs[5]+vs[7],vs

=======
Suggestion 10

def problem128_d():
    n,k = map(int,input().split())
    v = list(map(int,input().split()))
    ans = 0
    for l in range(min(n,k)+1):
        for r in range(min(n,k)-l+1):
            t = v[:l]+v[n-r:]
            t.sort()
            ans = max(ans,sum(t[max(0,k-l-r):]))
    print(ans)
