Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 3

def main():
    N = int(input())
    d = list(map(int,input().split()))
    res = 0
    for i in range(N):
        for j in range(i+1,N):
            res += d[i] * d[j]
    print(res)

=======
Suggestion 4

def takoyaki_festival():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i, N):
            sum += d[i] * d[j]
    print(int(sum / 2))

=======
Suggestion 6

def takoyaki():
    N = int(input())
    D = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        for j in range(i+1, N):
            sum += D[i] * D[j]
    return sum

=======
Suggestion 7

def main():
    #input
    N = int(input())
    d = list(map(int, input().split()))

    #compute
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += d[i] * d[j]

    #output
    print(ans)

=======
Suggestion 8

def takoyaki():
    n = int(input())
    d = [int(x) for x in input().split()]
    sum = 0
    for i in range(n):
        for j in range(i+1,n):
            sum += d[i] * d[j]
    return sum

print(takoyaki())

=======
Suggestion 9

def takoyaki_festival():
    N = int(input())
    d = list(map(int, input().split()))
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            result += d[i] * d[j]
    print(result)
