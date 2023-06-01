Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int,input().split()))
    print(len(set(a)))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    print(len(set(a)))

=======
Suggestion 3

def get_num():
    N = input()
    a = raw_input()
    a = a.split(' ')
    a = map(int, a)
    a.sort()
    a.append(0)
    count = 1
    for i in range(1, N):
        if a[i] != a[i - 1]:
            count += 1
    print count

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = input()
    a = map(int, raw_input().split())
    a = list(set(a))
    print len(a)
