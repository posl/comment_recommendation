Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i < n-1:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] == i:
            count += 1
    if count == n:
        print(n)
    else:
        print(n - 1)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if p[i] == i:
            cnt += 1
    if cnt == n:
        print(n)
        exit(0)
    if cnt == n-1:
        print(n-1)
        exit(0)
    if cnt == n-2:
        print(n-2)
        exit(0)
    if cnt == n-3:
        print(n-3)
        exit(0)
    if cnt == n-4:
        print(n-4)
        exit(0)
    if cnt == n-5:
        print(n-5)
        exit(0)
    print(n-6)
    exit(0)

=======
Suggestion 4

def solve():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if P[i] == i:
            ans += 1
            if i < N - 1:
                P[i], P[i + 1] = P[i + 1], P[i]
                if P[i] == i:
                    ans += 1
            else:
                P[i], P[0] = P[0], P[i]
                if P[i] == i:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i != n-1:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i+1 < N:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            if i == N-1:
                p[0], p[i] = p[i], p[0]
            else:
                p[i+1], p[i] = p[i], p[i+1]
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
  N = int(input())
  P = list(map(int, input().split()))
  count = 0
  for i in range(N):
    if P[i] == i:
      count += 1
  if count == N:
    print(N)
  else:
    print(N-1)

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    p.append(0)
    ans = 0
    for i in range(1, n+1):
        if p[i-1] < p[i] < p[i+1] or p[i-1] > p[i] > p[i+1]:
            ans += 1
    print(ans)
main()

=======
Suggestion 10

def solve():
    N = int(input())
    P = [int(x) for x in input().split()]
    #print(N, P)
    count = 0
    for i in range(N):
        if i == P[P[i]]:
            count += 1
    #print(count)
    if count == N:
        print(N)
    else:
        print(count-1)
