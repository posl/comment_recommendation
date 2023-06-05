Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    prev = 0
    for i in range(n):
        if a[i] != prev:
            ans += 1
            prev = a[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(len(set(a)))

=======
Suggestion 4

def main():
    num = int(input())
    data = list(map(int,input().split()))
    print(len(set(data)))

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))
