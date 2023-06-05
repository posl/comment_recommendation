Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    d = list(map(int, input().split()))
    sum_d = 0
    for i in range(n):
        sum_d += d[i]
    sum_d = sum_d**2
    sum_d2 = 0
    for i in range(n):
        sum_d2 += d[i]**2
    print((sum_d-sum_d2)//2)

=======
Suggestion 2

def main():
    N = int(input())
    d = list(map(int,input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1,N):
            sum += d[i]*d[j]
    print(sum)

=======
Suggestion 3

def main():
    n = int(input())
    d = list(map(int, input().split()))
    print(sum([d[i] * d[j] for i in range(n) for j in range(i + 1, n)]))

=======
Suggestion 4

def main():
    n=int(input())
    d=list(map(int,input().split()))
    sum=0
    for i in range(n):
        for j in range(i+1,n):
            sum+=d[i]*d[j]
    print(sum)

=======
Suggestion 5

def solve():
    n = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += d[i] * d[j]
    print(ans)
