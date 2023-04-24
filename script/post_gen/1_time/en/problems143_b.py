Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            ans += d[i] * d[j]
    print(ans)

main()

=======
Suggestion 3

def main():
    n = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    d = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 5

def takoyaki_festival():
    N = int(input())
    d = [int(x) for x in input().split()]
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 6

def takoyaki_fest(n, d):
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    return sum

=======
Suggestion 7

def takoyaki_festival():
    n = int(input())
    dish = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += dish[i] * dish[j]
    print(sum)

takoyaki_festival()

=======
Suggestion 8

def takoyaki_festival(N, d):
    sum = 0
    for i in range(N):
        for j in range(i+1,N):
            sum += d[i]*d[j]
    return sum
