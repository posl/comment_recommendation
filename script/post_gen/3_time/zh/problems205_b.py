Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = input().split()
    a = set(a)
    if len(a) == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == list(range(1, n+1)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    a = input().split()
    b = [int(i) for i in a]
    b.sort()
    if b == list(range(1, n+1)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def is_permutation(n, a):
    for i in range(1, n+1):
        if i not in a:
            return False
    return True

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] != i + 1:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == list(range(1, n + 1)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def is_permutation(n, seq):
    if n != len(seq):
        return False
    seq.sort()
    if seq[0] != 1:
        return False
    for i in range(1, n):
        if seq[i] - seq[i - 1] != 1:
            return False
    return True


n = int(input())
seq = list(map(int, input().split()))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if a[i] > n:
            print("No")
            return
        b[a[i] - 1] += 1
    for i in range(n):
        if b[i] != 1:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n+1):
        if a[i-1] != i:
            print('No')
            break
        if i == n:
            print('Yes')
