Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(N):
        if A[i] % 2 == 0:
            print(A[i])
            return
    print(-1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[0] % 2 == 0:
        print(A[0])
    else:
        for i in range(1, N):
            if A[i] % 2 == 0:
                print(A[i])
                break
        else:
            print(-1)

=======
Suggestion 3

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
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[0] % 2 == 0:
        print(A[0])
    else:
        for i in range(1, N):
            if A[i] % 2 == 0:
                print(A[i])
                break
        else:
            print(-1)

main()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[0] % 2 == 0:
        print(A[0])
    else:
        for i in range(1, N):
            if A[i] % 2 == 0:
                print(A[i])
                return
        print(-1)

=======
Suggestion 6

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
                return
        print(-1)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = -1
    for i in range(n-1):
        if (a[i] + a[i+1]) % 2 == 0:
            ans = a[i] + a[i+1]
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    ans = -1
    for i in range(n):
        if a[i]%2 == 0:
            ans = a[i]
            break
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    for i in range(1, N):
        if A[i] % 2 == 0:
            print(B[N] - B[i])
            return
    print(-1)

=======
Suggestion 10

def main():
    N=int(input())
    A=list(map(int,input().split()))

    # 偶数の数を数える
    cnt_even=0
    for a in A:
        if a%2==0:
            cnt_even+=1

    if cnt_even%2==0:
        print(-1)
    else:
        print(max(A))
