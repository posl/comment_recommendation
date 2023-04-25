Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        A -= K
    else:
        K -= A
        A = 0
        if B >= K:
            B -= K
    print(A, B)

=======
Suggestion 2

def main():
    A, B, K = map(int, input().split())

    if A >= K:
        print(A - K, B)
    elif A + B >= K:
        print(0, A + B - K)
    else:
        print(0, 0)

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    if A + B <= K:
        print(0, 0)
    elif A >= K:
        print(A - K, B)
    else:
        print(0, A + B - K)

main()

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        print(A - K, B)
    elif B >= K - A:
        print(0, B - (K - A))
    else:
        print(0, 0)

=======
Suggestion 5

def main():
    a, b, k = map(int, input().split())
    if k <= a:
        print(a - k, b)
    else:
        print(0, max(0, b - (k - a)))

main()

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        print(A-K, B)
    else:
        print(0, max(0, B-(K-A)))

=======
Suggestion 7

def main():
    a, b, k = map(int, input().split())
    if k <= a:
        a -= k
    else:
        k -= a
        a = 0
        b -= k
        if b <= 0:
            b = 0
    print(a, b)

=======
Suggestion 8

def main():
    A,B,K = map(int,input().split())
    if A>=K:
        A-=K
    else:
        K-=A
        A=0
        B-=K
        if B<0:
            B=0
    print(A,B)

=======
Suggestion 9

def main():

    #Read the input
    A,B,K = map(int,input().split())

    #If K is smaller than A, then Takahashi will eat K cookies, and Aoki will eat nothing.
    if K < A:
        A -= K
    #If K is larger than A, then Takahashi will eat all of his cookies, and Aoki will eat K-A cookies.
    elif K > A:
        B -= (K-A)
        A = 0
    #If K is equal to A, then Takahashi will eat all of his cookies, and Aoki will eat nothing.
    else:
        A = 0

    #Output the result
    print(A,B)
