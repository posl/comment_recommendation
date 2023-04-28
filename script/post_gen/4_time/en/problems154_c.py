Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) == len(set(a)):
        print('YES')
    else:
        print('NO')

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) == len(set(A)):
        print("YES")
    else:
        print("NO")

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            print("NO")
            return
    print("YES")
    return

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == len(a):
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n):
        if a[i] == a[i-1]:
            print("NO")
            return
    print("YES")
    return

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if len(a) == len(set(a)) else "NO")

=======
Suggestion 7

def main():
  n = int(input())
  a = list(map(int, input().split()))
  a.sort()
  for i in range(n-1):
    if a[i] == a[i+1]:
      print("NO")
      exit()
  print("YES")

=======
Suggestion 8

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    if len(set(A)) == N:
        print('YES')
    else:
        print('NO')

=======
Suggestion 9

def main():
    n = input()
    n = int(n)
    a = input().split()
    a = [int(m) for m in a]
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print('NO')
            return
    print('YES')
