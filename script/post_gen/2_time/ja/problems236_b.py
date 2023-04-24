Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * (N + 1)
    for a in A:
        cnt[a] += 1
    for i in range(1, N + 1):
        if cnt[i] % 2 == 1:
            print(i)
            break

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(0, 4*N-1, 2):
        if A[i] != A[i+1]:
            print(A[i])
            break
    else:
        print(A[-1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(0, 4*N-1, 2):
        if A[i] != A[i+1]:
            print(A[i])
            break

=======
Suggestion 4

def main():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    for i in c:
        if c[i] == 1:
            print(i)
            break

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = set()
    for i in range(len(A)):
        if A[i] in S:
            S.remove(A[i])
        else:
            S.add(A[i])
    print(S.pop())

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(4*N-1):
        if A[i] == A[i+1]:
            i += 1
        else:
            print(A[i])
            break

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    for i in range(4*n-1):
        if a[i] != a[i+1]:
            print(a[i])
            return
        else:
            i += 3

=======
Suggestion 8

def main():
    N = int(input())
    card = list(map(int, input().split()))
    card.sort()
    for i in range(4*N-1):
        if card[i] != card[i+1]:
            print(card[i])
            break
        else:
            i += 1

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    B = []
    for i in range(1,N+1):
        B.append(A.count(i))
    #print(B)
    for i in range(len(B)):
        if B[i] == 1:
            print(i+1)
