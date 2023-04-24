Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-1, 0, -1):
        ans = max(ans, p[i-1])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-1, 0, -1):
        ans += 1
        if p[i-1] == 1:
            break
        else:
            i = p[i-1]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    ans = 0
    current = n
    while current != 1:
        current = parents[current - 2]
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N-1, 0, -1):
        if P[i] > P[i-1]:
            ans += 1
        else:
            ans = 0
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    p.insert(0,0)
    ans = 0
    for i in range(1,n+1):
        ans = max(ans, p[i])
        for j in range(ans):
            p[i] = p[p[i]]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int,input().split()))
    P.insert(0,0)
    count = 0
    for i in range(N,1,-1):
        if P[i] == 1:
            count += 1
            break
        else:
            count += 1
            i = P[i]
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int,input().split()))
    if n==2:
        print(1)
        return
    p.insert(0,0)
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[p[i-1]]+1
    print(max(dp))

main()

=======
Suggestion 8

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    p.insert(0, None)
    print(max([p.count(i) for i in range(1, n + 1)]))

=======
Suggestion 9

def findParent(parents, p):
    if parents[p] == p:
        return p
    else:
        return findParent(parents, parents[p])

=======
Suggestion 10

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    parents.insert(0,0)

    #print(parents)
    #print(parents[n])

    count = 0
    while parents[n] != 1:
        n = parents[n]
        count += 1

    print(count+1)
