Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    happiness = [0]*N
    for i in range(N):
        happiness[(p[i]-1)%N] += 1
    print(max(happiness))

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    p.insert(N+1, 0)
    p.insert(N+2, 0)
    ans = 0
    for i in range(1, N+1):
        if p[i-1] < p[i] < p[i+1] or p[i-1] > p[i] > p[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def get_max_happy_person_number(n, p):
    happy_person_number = 0
    for i in range(0, n):
        if i == 0:
            if p[n-1] == i or p[i] == i or p[i+1] == i:
                happy_person_number += 1
        elif i == n-1:
            if p[i-1] == i or p[i] == i or p[0] == i:
                happy_person_number += 1
        else:
            if p[i-1] == i or p[i] == i or p[i+1] == i:
                happy_person_number += 1
    return happy_person_number

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p2 = list(map(lambda x: x-1, p))
    happy = 0
    for i in range(N):
        if p2[p2[i]] == i:
            happy += 1
    print(happy)

main()

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)
    P.append(0)
    #print(P)
    ans = 0
    for i in range(1, N+1):
        if P[i-1] < P[i] < P[i+1] or P[i+1] < P[i] < P[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    p = list(map(int,input().split()))
    #print(N)
    #print(p)
    cnt = 0
    for i in range(N):
        if p[i] == i:
            cnt += 1
    if cnt == N:
        print(N)
    else:
        print(cnt + 2*(N-cnt)//3)

=======
Suggestion 7

def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    print(N)
    print(p)

=======
Suggestion 8

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] == i:
            count += 1
        else:
            if p[p[i]] == i:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i]] = i
    ans = 0
    right = 0
    for i in range(N):
        if Q[i] > right:
            ans += 1
        right = Q[i]
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    p = list(map(lambda x: int(x)-1, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            if i < n-1:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
            ans += 1
    print(ans)
