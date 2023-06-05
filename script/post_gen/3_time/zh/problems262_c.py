Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i + 1 == a[a[i] - 1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def count_pairs(a):
    n = len(a)
    pairs = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if min(a[i - 1], a[j - 1]) == i and max(a[i - 1], a[j - 1]) == j:
                pairs += 1
    return pairs

=======
Suggestion 4

def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * N
    for i in range(N):
        if a[i] - i - 1 >= 0:
            b[a[i] - i - 1] += 1
    ans = 0
    for i in range(N):
        if a[i] + i + 1 <= N:
            ans += b[a[i] + i]
    print(ans)

=======
Suggestion 5

def main():
  n = int(input())
  a = list(map(int, input().split()))
  ans = 0

  for i in range(n):
    if a[i] == i + 1:
      continue
    if a[a[i] - 1] == i + 1:
      ans += 1

  print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #a = [1,3,2,4]
    #a = [5,8,2,2,1,6,7,2,9,10]
    #n = 10
    count = 0
    for i in range(1, n):
        if a[i-1] == i:
            for j in range(i+1, n+1):
                if a[j-1] == j:
                    count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if min(a[i-1], a[j-1]) == i and max(a[i-1], a[j-1]) == j:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a = [0] + a
    ans = 0
    for i in range(1, n + 1):
        if a[a[i]] == i:
            ans += 1
    print(ans)

=======
Suggestion 9

def problems262_c():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if a[i] - 1 < n:
            b[a[i] - 1] = i
    ans = 0
    for i in range(n - 1):
        if b[i] > b[i + 1]:
            ans += 1
    print(ans * 2)
