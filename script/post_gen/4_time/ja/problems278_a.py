Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(*a)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(" ".join(map(str, a)))

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(k):
        a.pop(0)
        a.append(0)
    print(*a)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    for i in a:
        print(i, end=' ')
    print()

=======
Suggestion 5

def problems278_a():
    #input
    n,k = map(int,input().split())
    a = list(map(int,input().split()))

    #calculate
    for i in range(k):
        a.pop(0)
        a.append(0)

    #output
    print(*a)

=======
Suggestion 6

def check():
    if 1 <= N and N <= 100 and 1 <= K and K <= 100:
        return True
    else:
        return False
