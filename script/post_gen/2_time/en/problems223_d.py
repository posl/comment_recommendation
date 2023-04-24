Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(' '.join(map(str, solve(N, M, A, B))))

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    ans = [0] * N
    for i in range(N):
        ans[i] = i
    for i in range(M):
        if A[i] == 0:
            A[i], B[i] = B[i], A[i]
        else:
            A[i] -= 1
            B[i] -= 1
    for i in range(M):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
    for i in range(M):
        if ans[A[i]] > ans[B[i]]:
            ans[A[i]], ans[B[i]] = ans[B[i]], ans[A[i]]
    for i in range(N):
        if ans[i] == i:
            print(-1)
            return
    print(*[x + 1 for x in ans])

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    if 1 in a:
        print(-1)
    else:
        print(1)
    return

=======
Suggestion 4

def solve():
  n, m = map(int, input().split())
  a = [0] * m
  b = [0] * m
  for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
  ans = [-1] * n
  ans[0] = 0
  for i in range(m):
    if ans[a[i]] == -1:
      ans[a[i]] = ans[b[i]]
    elif ans[b[i]] == -1:
      ans[b[i]] = ans[a[i]]
    else:
      if ans[a[i]] == ans[b[i]]:
        print(-1)
        return
      else:
        if ans[a[i]] == 0:
          ans[b[i]] = 1
        else:
          ans[b[i]] = 0
  for i in range(n):
    if ans[i] == -1:
      ans[i] = 0
  ans = [x + 1 for x in ans]
  print(*ans)
  return

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        c,d = map(int,input().split())
        a.append(c)
        b.append(d)
    a.sort()
    b.sort()
    if a[-1] > b[0]:
        print(-1)
    else:
        print(a[-1],b[0])

=======
Suggestion 6

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print(type(N), type(M))
    #print(type(N), type(M))
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)

=======
Suggestion 8

def find_set(a):
    if a != parent[a]:
        parent[a] = find_set(parent[a])
    return parent[a]

=======
Suggestion 9

def main():
    pass
