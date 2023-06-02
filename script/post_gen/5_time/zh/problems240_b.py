Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 1
    for i in range(1, N):
        if a[i] != a[i - 1]:
            cnt += 1
    print(cnt)

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
    a = list(map(int, input().split()))

    # a = [1, 4, 1, 2, 2, 1]
    # a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    a.sort()
    # print(a)
    # print(len(a))

    count = 1
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            count += 1

    print(count)

=======
Suggestion 4

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(1, N):
        if a[i] != a[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    a = input().split()
    print(len(set(a)))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

main()
