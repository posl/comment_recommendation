Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i] + a[j] + a[k] <= w:
                    ans += 1
    print(ans)

=======
Suggestion 2

def solve():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [0] * (w + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(w, -1, -1):
            if dp[j] == 1:
                if j + a[i] <= w:
                    dp[j + a[i]] = 1
    print(sum(dp))

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for a in range(N + 1):
        for b in range(N + 1):
            for c in range(N + 1):
                for d in range(N + 1):
                    for e in range(N + 1):
                        for f in range(N + 1):
                            for g in range(N + 1):
                                if a + b + c + d + e + f + g > N:
                                    continue
                                if a * A[0] + b * A[1] + c * A[2] + d * A[3] + e * A[4] + f * A[5] + g * A[6] <= W:
                                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n,w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i,n):
            for k in range(j,n):
                if a[i] + a[j] + a[k] <= w:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 5

def get_good_integers(n, w, a):
    good_integers = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                good_integers.add(a[i])
                good_integers.add(a[j])
                good_integers.add(a[k])
                good_integers.add(a[i] + a[j])
                good_integers.add(a[i] + a[k])
                good_integers.add(a[j] + a[k])
                good_integers.add(a[i] + a[j] + a[k])
    good_integers = [x for x in good_integers if x <= w]
    return len(good_integers)

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    weight = [0] * N
    for i in range(N):
        if A[i] <= W:
            weight[i] = 1
    #print(weight)
    total = 0
    for i in range(N):
        if weight[i] == 1:
            total += 1
    #print(total)
    for i in range(N-1):
        for j in range(i+1, N):
            if weight[i] == 1 and weight[j] == 1 and A[i] + A[j] <= W:
                total += 1
    #print(total)
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if weight[i] == 1 and weight[j] == 1 and weight[k] == 1 and A[i] + A[j] + A[k] <= W:
                    total += 1
    print(total)

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    #print(A)
    a = A[0]
    b = A[1]
    c = A[2]
    d = A[3]
    e = A[4]
    f = A[5]
    g = A[6]
    count = 0
    for i in range(W//a + 1):
        for j in range((W - a*i)//b + 1):
            for k in range((W - a*i - b*j)//c + 1):
                for l in range((W - a*i - b*j - c*k)//d + 1):
                    for m in range((W - a*i - b*j - c*k - d*l)//e + 1):
                        for n in range((W - a*i - b*j - c*k - d*l - e*m)//f + 1):
                            for o in range((W - a*i - b*j - c*k - d*l - e*m - f*n)//g + 1):
                                if a*i + b*j + c*k + d*l + e*m + f*n + g*o <= W:
                                    count += 1
                                else:
                                    break
    print(count)

=======
Suggestion 8

def main():
    #input
    N, W = map(int, input().split())
    A = list(map(int, input().split()))

    #algorithm
    A.sort()
    A = [0] + A
    dp = [[0] * (W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j - A[i] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i]] + A[i])
            else:
                dp[i][j] = dp[i-1][j]

    #output
    print(sum(dp[N]))

=======
Suggestion 9

def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, w)
    #print(a)
    
    # 3つの重さを選ぶ
    # 重さの合計がw以下のものをカウントする
    # 重さ��

=======
Suggestion 10

def search(possible, target, total, n):
    if total == target:
        return 1
    elif total > target or n == len(possible):
        return 0
    else:
        return search(possible, target, total + possible[n], n + 1) + search(possible, target, total, n + 1)
