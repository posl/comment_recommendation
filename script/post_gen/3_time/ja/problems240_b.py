Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 1
    for i in range(N-1):
        if a[i] != a[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(len(set(A)))

=======
Suggestion 5

def main():
    N = int(input())
    a = [int(x) for x in input().split()]
    print(len(set(a)))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    print(len(s))

=======
Suggestion 7

def main():
    N = int(input())
    a = list(map(int, input().split()))

    # setを使って重複を削除
    print(len(set(a)))
