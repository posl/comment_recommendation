Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if a[i] < P:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] < P:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([i for i in a if i < P]))

=======
Suggestion 5

def main():
    N, P = map(int, input().split())
    L = list(map(int, input().split()))
    count = 0
    for i in range(0, N):
        if L[i] < P:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, p)
    # print(a)
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n, p = map(int, input().split())
    A = list(map(int, input().split()))
    print(sum([1 for a in A if a < p]))

=======
Suggestion 8

def main():
    # Read input
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Count number of students who failed the exam
    num_failed = 0
    for i in range(n):
        if a[i] < p:
            num_failed += 1
    
    # Print the number of students who failed the exam
    print(num_failed)
