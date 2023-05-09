Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    W = [int(x) for x in input().split()]
    W1 = [W[i] for i in range(N) if S[i] == '1']
    W0 = [W[i] for i in range(N) if S[i] == '0']
    W1.sort()
    W0.sort()
    if len(W1) == 0 or len(W0) == 0:
        print(0)
        return
    W1sum = [0] * (len(W1) + 1)
    W0sum = [0] * (len(W0) + 1)
    for i in range(len(W1)):
        W1sum[i+1] = W1sum[i] + W1[i]
    for i in range(len(W0)):
        W0sum[i+1] = W0sum[i] + W0[i]
    ans = 0
    for i in range(len(W1) + 1):
        for j in range(len(W0) + 1):
            if W1sum[i] + W0sum[j] <= 2 * (i + j):
                ans = max(ans, i + j)
    print(ans)

=======
Suggestion 2

def get_input():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    return N, S, W

=======
Suggestion 3

def solve():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] == '1':
            ans += w[i]
    ans2 = ans
    for i in range(n):
        if s[i] == '1':
            ans2 -= w[i]
            ans = max(ans, ans2)
        else:
            ans2 += w[i]
            ans = max(ans, ans2)
    print(ans)

solve()

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    max = 0
    for i in range(0, N):
        if S[i] == '0':
            if max < W[i]:
                max = W[i]
    print(max)

=======
Suggestion 5

def f(X):
    if X < 50:
        return 0
    elif X >= 50 and X < 100:
        return 1
    elif X >= 100 and X < 150:
        return 2
    elif X >= 150 and X < 200:
        return 3
    elif X >= 200 and X < 250:
        return 4
    elif X >= 250 and X < 300:
        return 5
    elif X >= 300 and X < 350:
        return 6
    elif X >= 350 and X < 400:
        return 7
    elif X >= 400 and X < 450:
        return 8
    elif X >= 450 and X < 500:
        return 9
    elif X >= 500 and X < 550:
        return 10
    elif X >= 550 and X < 600:
        return 11
    elif X >= 600 and X < 650:
        return 12
    elif X >= 650 and X < 700:
        return 13
    elif X >= 700 and X < 750:
        return 14
    elif X >= 750 and X < 800:
        return 15
    elif X >= 800 and X < 850:
        return 16
    elif X >= 850 and X < 900:
        return 17
    elif X >= 900 and X < 950:
        return 18
    elif X >= 950 and X < 1000:
        return 19
    elif X >= 1000:
        return 20

n = int(input())
s = input()
w = list(map(int,input().split()))
ans = 0
for i in range(n):
    if s[i] == '1':
        ans += f(w[i])
print(ans)

=======
Suggestion 6

def solve(n, s, w):
    ans = 0
    for i in range(n):
        if s[i] == '0':
            ans += w[i]
    ans2 = ans
    for i in range(n):
        if s[i] == '1':
            ans2 += w[i]
    return max(ans, ans2)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    #print(n, s, w)
    l = 0
    r = n
    while l + 1 < r:
        mid = (l + r) // 2
        #print(l, r, mid)
        if check(mid, n, s, w):
            l = mid
        else:
            r = mid
    print(l)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    S = list(map(int, S))
    S.append(0)
    W.append(0)
    S.append(0)
    W.append(0)
    
    #print(S)
    #print(W)
    
    # 0: child
    # 1: adult
    # 2: ?
    # 3: ?
    
    # N = 5
    # S = [1,0,1,0,1]
    # W = [60,45,30,40,80]
    # S = [1,0,1,0,1,0,0]
    # W = [60,45,30,40,80,0,0]
    
    # S = [1,0,1,0,1,0,0,0]
    # W = [60,45,30,40,80,0,0,0]
    
    # S = [1,0,1,0,1,0,0,0,0]
    # W = [60,45,30,40,80,0,0,0,0]
    
    # S = [0,0,0,0,0,0,0,0,0]
    # W = [60,45,30,40,80,0,0,0,0]
    
    # S = [1,1,1,1,1,1,1,1,1]
    # W = [60,45,30,40,80,0,0,0,0]
    
    # S = [0,0,0,0,0,0,0,0,0]
    # W = [60,45,30,40,80,0,0,0,0]
    
    # S = [1,0,1,0,1,0,0,0,0]
    # W = [60,45,30,40,80,0,0,0,0]
    
    # S = [1,0,1,0,1,0,0,0,0]
    # W = [60,45,30,40,80,0,0,0,0]
    
    # S

=======
Suggestion 9

def main():
    # Get input
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    
    # Initialize variables
    ans = 0
    w = 0
    wsum = sum(W)
    for i in range(N):
        if S[i] == '0':
            w += W[i]
        else:
            ans = max(ans, wsum-w)
    print(ans)

=======
Suggestion 10

def countAdults(children, adults, X):
    if children >= X:
        return adults
    else:
        return adults + children - X
