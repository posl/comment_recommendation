Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    min = N + 1
    count = 0
    for i in range(N):
        if min > P[i]:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    min = n+1
    count = 0
    for i in range(n):
        if min > p[i]:
            min = p[i]
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    min = 0
    cnt = 0
    for i in range(N):
        if P[i] >= min:
            cnt += 1
            min = P[i]
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int,input().split()))
    count = 0
    min = N + 1
    for i in P:
        if min > i:
            min = i
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N)
    #print(P)
    count = 0
    min = N + 1
    for i in range(N):
        if min >= P[i]:
            min = P[i]
            count += 1
    print(count)
main()

=======
Suggestion 6

def main():
    n = input()
    p = [int(x) for x in input().split()]
    min = p[0]
    count = 1
    for i in range(1, int(n)):
        if p[i] <= min:
            count += 1
            min = p[i]
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min = p[0]
    for i in range(0, n):
        if p[i] <= min:
            count += 1
            min = p[i]
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    min = N
    count = 0
    for i in range(N):
        if min > P[i]:
            min = P[i]
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_min = n+1
    count = 0
    for i in range(n):
        if p[i] <= p_min:
            count += 1
            p_min = p[i]
    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min = 10**6
    for i in range(N):
        if P[i] < min:
            ans += 1
            min = P[i]
    print(ans)
