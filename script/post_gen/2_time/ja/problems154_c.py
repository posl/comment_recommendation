Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            print("NO")
            return
    print("YES")

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            print('NO')
            return
    print('YES')
    return

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            print("NO")
            exit()
    print("YES")

=======
Suggestion 6

def main():
  n = int(input())
  a = list(map(int,input().split()))
  a.sort()
  for i in range(n-1):
    if a[i] == a[i+1]:
      print('NO')
      return
  print('YES')
  return

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))

    if len(set(a)) == n:
        print('YES')
    else:
        print('NO')

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    a.sort()
    #print(a)
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            return
    print("YES")
