Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if len(A) == 2:
        if (A[0] + A[1]) % 2 == 0:
            print(A[0] + A[1])
        else:
            print(-1)
    else:
        for i in range(1, len(A)):
            if (A[i] + A[i-1]) % 2 == 0:
                print(A[i] + A[i-1])
                break
        else:
            print(-1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    even = -1
    for i in range(N-1):
        if A[i] == A[i+1]:
            even = A[i]
            break
    print(even*2)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max_even = -1
    for i in range(n-1, 0, -1):
        if a[i] % 2 == 0:
            if a[i] == a[i-1]:
                max_even = a[i]
                break
            elif a[i] - 1 == a[i-1]:
                max_even = a[i]
                break
    print(max_even)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    #print(a)
    for i in range(n):
        for j in range(i+1,n):
            if (a[i]+a[j])%2==0:
                print(a[i]+a[j])
                return
    print(-1)
    return

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #print(A)
    max_even = -1
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                max_even = max(max_even, A[i] + A[j])
    print(max_even)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    B = [A[0]]
    for i in range(1,N):
        if A[i] == A[i-1]:
            B.append(A[i])
        else:
            if len(B) >= 2:
                if B[-1] % 2 == 0:
                    print(B[-1])
                    return
                else:
                    B.pop()
            B.append(A[i])
    print(-1)

=======
Suggestion 7

def main():
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = [a[0]]
    for i in range(1, n):
        if a[i] == a[i - 1]:
            b.append(a[i])
        elif a[i] + a[i - 1] in b:
            return print(a[i] + a[i - 1])
    print(-1)
main()

=======
Suggestion 8

def main():
    # input
    n = int(input())
    a = list(map(int, input().split()))
    # compute
    a.sort()
    if a[0] == 0:
        print(-1)
    else:
        print(a[-1] + a[-2])
    # output

=======
Suggestion 9

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))

    # compute
    A.sort()
    A.reverse()
    B = []
    for i in range(N-1):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                B.append(A[i] + A[j])
    if len(B) == 0:
        print(-1)
    else:
        print(max(B))

=======
Suggestion 10

def main():
    #input
    n = int(input())
    a = list(map(int, input().split()))

    #process
    a.sort(reverse=True)
    max_even = -1
    for i in range(n):
        if a[i] % 2 == 0:
            max_even = a[i]
            break
    if max_even == -1:
        print(-1)
        exit()
    for i in range(n):
        if a[i] % 2 == 0 and a[i] < max_even * 2:
            print(max_even)
            exit()
    print(-1)
