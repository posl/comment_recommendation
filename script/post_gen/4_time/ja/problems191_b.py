Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        if A[i] != X:
            B.append(A[i])
    print(*B)

=======
Suggestion 2

def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[i] != x:
            ans.append(a[i])
    print(*ans)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[i] == x:
            continue
        ans.append(str(a[i]))
    print(' '.join(ans))

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a_ = []
    for i in range(n):
        if a[i] != x:
            a_.append(a[i])
    for i in range(len(a_)):
        print(a_[i], end=" ")
    print()

=======
Suggestion 5

def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=" ")

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    for a in a_list:
        if a != x:
            print(a, end=' ')
    print()

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    for i in A:
        if i == X:
            continue
        else:
            print(i, end=" ")

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(*[i for i in A if i != X])

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(*[i for i in a if i != x])
    #print(*[i for i in a if i != x]) は print(*[i for i in a if i != x]) と同じ
    #print(*[i for i in a if i != x]) は print(*[i for i in a if i != x]) と同じ
    #print(*[i for i in a if i != x]) は print(*[i for i in a if i != x]) と同じ
    #print(*[i for i in a if i != x]) は print(*[i for i in a if i != x]) と同じ
    #print(*[i for i in a if i != x]) は print(*[i for i in a if i != x]) と同じ
    #print(*[i for i in a if i != x]) は print(*[i for i in a if i != x]) と同じ
    #print(*[i for i in a if i != x]) は print(*[i for i in a if i != x]) と同じ
    #print(*[i for i in a if i != x]) は print(*[i for i in a if i != x]) と同じ

=======
Suggestion 10

def get_input():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    return n, x, a
