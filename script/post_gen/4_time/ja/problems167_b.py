Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    else:
        print(a - (k - a - b))

=======
Suggestion 2

def main():
    A, B, C, K = map(int, input().split())
    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 3

def main():
    a,b,c,k = map(int,input().split())
    if a >= k:
        print(k)
    elif a+b >= k:
        print(a)
    else:
        print(a-(k-a-b))

=======
Suggestion 4

def main():
    a,b,c,k = map(int,input().split())
    if a >= k:
        print(k)
    elif a+b >= k:
        print(a)
    else:
        print(a-(k-(a+b)))

=======
Suggestion 5

def main():
    a,b,c,k = map(int, input().split())
    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    else:
        print(a - (k - (a + b)))

=======
Suggestion 6

def main():
    a, b, c, k = map(int, input().split())
    answer = 0
    if a >= k:
        answer = k
    elif a + b >= k:
        answer = a
    else:
        answer = a - (k - a - b)
    print(answer)

=======
Suggestion 7

def main():
    a,b,c,k = map(int, input().split())
    print(min(a,k)-min(b,max(0,k-a)))
