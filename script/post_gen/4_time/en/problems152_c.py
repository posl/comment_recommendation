Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    minP = P[0]
    for i in range(N):
        if P[i] <= minP:
            cnt += 1
        minP = min(minP, P[i])
    print(cnt)

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    minP = float('inf')
    for i in range(N):
        if P[i] <= minP:
            count += 1
            minP = P[i]
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_P = N + 1
    for i in range(N):
        if P[i] < min_P:
            ans += 1
        min_P = min(min_P, P[i])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    counter = 0
    for i in range(N):
        if P[i] == min(P[:i+1]):
            counter += 1
    print(counter)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = N + 1
    for i in range(0, N):
        if P[i] <= min:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    minP = 1000000
    for i in range(N):
        if P[i] <= minP:
            count += 1
            minP = P[i]
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    maxP = P[0]
    count = 1
    for i in range(1,N):
        if maxP > P[i]:
            count += 1
        else:
            maxP = P[i]
    print(count)
    return

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min_value = n
    for i in range(n):
        if min_value > p[i]:
            min_value = p[i]
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N, P)
    #print(P.index(1))
    #print(P.index(2))
    #print(P.index(3))
    #print(P.index(4))
    #print(P.index(5))
    #print(P.index(6))
    #print(P.index(7))
    #print(P.index(8))
    cnt = 1
    min = P[0]
    for i in range(1, N):
        if min >= P[i]:
            cnt += 1
            min = P[i]
    print(cnt)

=======
Suggestion 10

def main():
    #input
    N = int(input())
    Ps = list(map(int,input().split()))

    #count
    count = 0
    min = N+1
    for i in range(N):
        if Ps[i] < min:
            count += 1
            min = Ps[i]

    #output
    print(count)

main()
