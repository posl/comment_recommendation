Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(1, n + 1):
        x = i
        while x != 1:
            ans[x // 2] = max(ans[x // 2], ans[x] + 1)
            x //= 2
    for i in range(1, 2 * n + 1):
        print(ans[i])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(2 * n - 1, 0, -1):
        ans[i // 2] += ans[i]
    for i in range(2 * n + 1):
        print(ans[i])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(2, 2 * n + 1):
        ans[i] = ans[i // 2] + 1
    for i in range(1, 2 * n + 1):
        print(ans[i])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * n + 1)
    for i in range(n):
        b[a[i]] = i + 1
    for i in range(1, 2 * n + 1):
        j = i
        while j <= 2 * n:
            b[j] = max(b[j], b[i] + 1)
            j += i
    for i in range(1, 2 * n + 1):
        print(b[i] - 1)

=======
Suggestion 5

def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=[0]*(2*n+1)
    for i in range(n):
        ans[a[i]]=i+1
    for i in range(2*n,0,-1):
        ans[i//2]+=ans[i]
    for i in range(2*n+1):
        print(ans[i])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0,0)
    ans = [0] * (2 * n + 1)
    for i in range(1, n + 1):
        ans[i] = 1
    for i in range(n, 0, -1):
        ans[i] += max(ans[2 * i], ans[2 * i + 1])
    for i in range(1, 2 * n + 1):
        print(ans[i])

=======
Suggestion 7

def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(1, n + 1):
        p = i
        cnt = 0
        while True:
            cnt += 1
            p = a[p]
            if p == 1:
                break
        ans[i] = cnt
    for i in range(1, 2 * n + 1):
        print(ans[i])

=======
Suggestion 8

def solve():
  n = int(input())
  a = [int(i) - 1 for i in input().split()]
  b = [0] * (2 * n + 1)
  for i in range(n):
    b[a[i]] = i + 1
  for i in range(2 * n - 1, 0, -1):
    b[i // 2] += b[i]
  for i in range(1, 2 * n + 1):
    print(b[i])

solve()

=======
Suggestion 9

def get_generation_distance(n, a):
    generation_distance = [0 for i in range(2*n+1)]
    generation_distance[1] = 0
    for i in range(n):
        generation_distance[2*(i+1)] = generation_distance[a[i]] + 1
        generation_distance[2*(i+1)+1] = generation_distance[a[i]] + 1
    return generation_distance

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
