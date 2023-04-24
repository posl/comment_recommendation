Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    b = sorted(a)
    #print(b)
    c = b[1]
    #print(c)
    d = a.index(c) + 1
    print(d)

=======
Suggestion 4

def main():
  n = int(input())
  a = list(map(int,input().split()))
  b = sorted(a)
  print(a.index(b[1])+1)
main()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sorted(A)[1])
