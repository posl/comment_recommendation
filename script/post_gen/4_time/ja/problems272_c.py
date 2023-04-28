Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == 0:
        print(-1)
    else:
        print(odd)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    odd = []
    even = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(odd) == 0:
        print(-1)
    else:
        print(sum(even) + min(odd) * (len(odd) - 1))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] % 2 == 0 or A[-1] % 2 == 0:
        print(A[-1])
    else:
        print(-1)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] % 2 == 0 or a[n-1] % 2 == 0:
        print(-1)
    else:
        print(a[n-1] + a[n-2])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    odd = [i for i in a if i % 2 == 1]
    if len(odd) == 0:
        print(-1)
    else:
        print(sum(a) - sum(odd))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0]%2 == 0 or a[-1]%2 == 0:
        print(a[-1])
    elif a[0]%2 != 0 and a[-1]%2 != 0:
        print(a[-1]+a[-2])
    else:
        print(-1)

=======
Suggestion 7

def check_even(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[i] + a[j]) % 2 == 0:
                return True
    return False

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    elif n == 2:
        print(-1)
    else:
        print(a[-1] + a[-2])

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    if A[0]%2 == 0:
        print(A[0])
        return
    if N == 1:
        print(-1)
        return
    if A[1]%2 == 0:
        print(A[1])
        return
    print(-1)

=======
Suggestion 10

def solve():
    # 解答を返す
    return
