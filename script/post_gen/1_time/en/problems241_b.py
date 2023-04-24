Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] >= B[j]:
            j += 1
        i += 1
    if j == M:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] >= B[j]:
            j += 1
        i += 1
    if j == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    j = 0
    for i in range(M):
        while j < N and A[j] < B[i]:
            j += 1
        if j == N or A[j] > B[i]:
            print("No")
            return
        j += 1
    print("Yes")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    if N < M:
        print("No")
        return
    for i in range(M):
        if B[i] > A[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for i in range(M):
        if B[i] > A[N-1]:
            print('No')
            return
        else:
            for j in range(N):
                if A[j] >= B[i]:
                    A[j] = 0
                    break
    print('Yes')

main()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(m):
        if a[i] < b[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    a = 0
    b = 0
    while a < N and b < M:
        if A[a] < B[b]:
            a += 1
        elif A[a] == B[b]:
            a += 1
            b += 1
        else:
            print("No")
            return
    if b == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(M):
        if B[i] in A:
            A.remove(B[i])
        else:
            print("No")
            return
    print("Yes")

solve()

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    for b in B:
        while i < N and A[i] < b:
            i += 1
        if i == N or A[i] > b:
            return "No"
        i += 1
    return "Yes"

print(solve())

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    if M > N:
        print("No")
        return
    for b in B:
        if b > A[-1]:
            print("No")
            return
        for i in range(len(A)):
            if A[i] >= b:
                A.pop(i)
                break
    print("Yes")
