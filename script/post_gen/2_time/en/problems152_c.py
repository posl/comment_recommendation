Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 1
    min = P[0]
    for i in range(1, N):
        if P[i] < min:
            min = P[i]
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = P[0]
    for i in range(N):
        if P[i] <= min:
            min = P[i]
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    minval = P[0]
    count = 1
    for i in range(1, N):
        if minval >= P[i]:
            minval = P[i]
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min_p = N + 1
    for i in range(N):
        if p[i] <= min_p:
            ans += 1
            min_p = p[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = 1000000
    for i in range(N):
        if P[i] < min:
            min = P[i]
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_val = 10**9
    for i in range(N):
        if P[i] <= min_val:
            ans += 1
            min_val = P[i]
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min = 10**6
    for i in p:
        if i <= min:
            ans += 1
            min = i
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    c = 0
    min = 1000000
    for i in range(N):
        if P[i] < min:
            c += 1
            min = P[i]
    print(c)

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N)
    #print(P)
    ans = 0
    minP = N+1
    for i in range(N):
        if P[i] <= minP:
            ans += 1
            minP = P[i]
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    P = [p - 1 for p in P]
    ans = 0

    min = N
    for p in P:
        if p < min:
            ans += 1
            min = p

    print(ans)
