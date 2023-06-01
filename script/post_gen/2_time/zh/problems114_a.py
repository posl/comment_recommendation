Synthesizing 10/10 solutions

=======
Suggestion 1

def amidakuji(h,w,k):
    if h==1:
        if k==1:
            return 1
        else:
            return 2
    else:
        if k==1:
            return 1
        elif k==w:
            return 1
        else:
            return amidakuji(h-1,w-1,k-1)+amidakuji(h-1,w-1,k)

=======
Suggestion 2

def amidakuji(h,w,k):
    if w==1:
        if h==1:
            return 1
        elif h==2:
            if k==1:
                return 1
            elif k==2:
                return 2
            else:
                return 0
        else:
            if k==1:
                return 1
            elif k==2:
                return 2
            elif k==3:
                return 4
            else:
                return 0
    else:
        if h==1:
            if k==1:
                return 1
            else:
                return 0
        elif h==2:
            if k==1:
                return 1
            elif k==2:
                return 2
            else:
                return 0
        else:
            if k==1:
                return 1
            elif k==2:
                return 2
            elif k==3:
                return 4
            elif k==4:
                return 8
            elif k==5:
                return 16
            else:
                return 0

h,w,k=map(int,input().split())
print(amidakuji(h,w,k))

=======
Suggestion 3

def main():
    H,W,K = map(int,input().split())
    #print(H,W,K)
    ans = 0
    dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
    dp[0][0] = 1
    MOD = 10**9+7
    for i in range(1,H+1):
        for j in range(W):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            dp[i][j] %= MOD
    #for i in range(H+1):
    #    print(dp[i])
    print(dp[H][K-1])

=======
Suggestion 4

def dfs(h,w,k):
    if w==1:
        if k==1:
            return 1
        else:
            return 0
    elif k==1:
        return dfs(h-1,w-1,1)
    elif k==w:
        return dfs(h-1,w-1,w-1)
    else:
        return dfs(h-1,w-1,k-1)+dfs(h-1,w-1,k)*(w-k)

=======
Suggestion 5

def amidakuji(h, w, k):
    if h == 1:
        return 1
    if k == 1:
        return amidakuji(h-1, w, k) + amidakuji(h-1, w, k+1)
    if k == w:
        return amidakuji(h-1, w, k-1) + amidakuji(h-1, w, k)
    return amidakuji(h-1, w, k-1) + amidakuji(h-1, w, k) + amidakuji(h-1, w, k+1)

=======
Suggestion 6

def amidakuji(h,w,k):
    a = [0 for i in range(w-1)]
    for i in range(w-1):
        a[i] = [0 for j in range(h+1)]
    for i in range(w-1):
        a[i][0] = 1
    for i in range(1,h+1):
        for j in range(w-1):
            if j == 0:
                a[j][i] = a[j][i-1] + a[j+1][i-1]
            elif j == w-2:
                a[j][i] = a[j-1][i-1] + a[j][i-1]
            else:
                a[j][i] = a[j-1][i-1] + a[j][i-1] + a[j+1][i-1]
    return a[k-1][h] % 1000000007

=======
Suggestion 7

def amidakuji(h,w,k):
    if w == 1:
        return 1
    if k == 1:
        return amidakuji(h-1,w-1,1)
    if k == w:
        return amidakuji(h-1,w-1,w-1)
    else:
        return amidakuji(h-1,w-1,k-1) + amidakuji(h-1,w-1,k)

h,w,k = map(int,input().split())
print(amidakuji(h,w,k)%1000000007)

=======
Suggestion 8

def amidakuji(h,w,k):
    if w==1:
        return 1
    if k==1:
        return amidakuji(h,w-1,1)+amidakuji(h,w-1,2)
    if k==w:
        return amidakuji(h,w-1,w-1)+amidakuji(h,w-1,w)
    return amidakuji(h,w-1,k-1)+amidakuji(h,w-1,k)+amidakuji(h,w-1,k+1)

h,w,k=map(int,input().split())
print(amidakuji(h,w,k)%1000000007)

=======
Suggestion 9

def amidakuji(h,w,k):
    if h==1:
        if k==1:
            return 1
        else:
            return 2
    elif h==2:
        if k==1:
            return 2
        elif k==2:
            return 5
        else:
            return 1
    else:
        if k==1:
            return 5
        elif k==2:
            return 12
        elif k==3:
            return 6
        elif k==4:
            return 2
        else:
            return 1

=======
Suggestion 10

def amidakuji(h,w,k):
    if w==1:
        return 1
    elif k==1:
        return amidakuji(h,w-1,1)+amidakuji(h,w-1,2)
    elif k==w:
        return amidakuji(h,w-1,w-1)+amidakuji(h,w-1,w)
    else:
        return amidakuji(h,w-1,k-1)+amidakuji(h,w-1,k)+amidakuji(h,w-1,k+1)

h,w,k=map(int,input().split())
print(amidakuji(h,w,k)%1000000007)
