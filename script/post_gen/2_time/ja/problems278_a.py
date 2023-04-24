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
    for i in range(n):
        print(a[i], end=" ")
    print()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(K):
        A.pop(0)
        A.append(0)
    print(*A)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    for j in range(N):
        if j == N-1:
            print(A[j])
        else:
            print(A[j], end=' ')

=======
Suggestion 5

def list_to_string(list):
    str = ""
    for i in range(len(list)):
        str += list[i]
        if i != len(list) - 1:
            str += " "
    return str
