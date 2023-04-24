Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
    else:
        for i in range(N-1):
            if A[i] % 2 == 1:
                print(A[i])
                break
        else:
            print(-1)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    else:
        for i in range(n-1):
            if a[i] % 2 == 0:
                print(a[i])
                break
        else:
            print(-1)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 1:
        print(-1)
    else:
        print(A[-1])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = -1
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] == A[i+1]:
                ans = A[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
        return
    for i in range(N-1):
        if A[i] % 2 == 0:
            print(A[i])
            return
    print(-1)

main()

The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.

The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.

The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.

The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.

The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.

The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.

The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.

The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.

The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.

The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.

The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.

The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.

The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.

The output should contain the maximum even number represented as the sum of two different elements of A.  If there is

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 1:
        a.pop()
    if len(a) % 2 == 1:
        a.pop()
    if len(a) == 0:
        print(-1)
    else:
        print(a[-1] + a[-2])

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    A.reverse()
    max_even = -1
    for i in range(N):
        for j in range(i+1,N):
            if (A[i] + A[j]) % 2 == 0:
                max_even = max(max_even, A[i] + A[j])
    print(max_even)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    if A[-1] % 2 == 1:
        print(-1)
        return

    if A[-1] == A[-2]:
        print(A[-1])
        return

    if A[-1] == A[-2] + 1:
        print(-1)
        return

    print(A[-1])

=======
Suggestion 9

def solve(n, a):
    if n == 2:
        if a[0] == a[1]:
            return -1
        else:
            return a[0] + a[1]
    a.sort()
    if a[-1] % 2 == 0:
        return a[-1]
    else:
        a[-1] -= 1
        return a[-1] + a[-2]
