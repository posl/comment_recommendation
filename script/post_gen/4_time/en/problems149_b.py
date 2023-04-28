Synthesizing 10/10 solutions

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

main()

I solved this problem in 10 minutes.

I thought that I could solve this problem by using the following logic:

If A is greater than K, then A will be reduced by K.

If A is less than or equal to K, then K will be reduced by A, and A will be reduced to 0.

If B is greater than or equal to K, then B will be reduced by K.

If B is less than K, then B will be reduced to 0.

I submitted my code, and it was accepted.

I think that this problem was very easy.

I will solve the next problem.

I have solved 1 problem.

I will solve the next problem.

I have solved 2 problems.

I will solve the next problem.

I have solved 3 problems.

I will solve the next problem.

I have solved 4 problems.

I will solve the next problem.

I have solved 5 problems.

I will solve the next problem.

I have solved 6 problems.

I will solve the next problem.

I have solved 7 problems.

I will solve the next problem.

I have solved 8 problems.

I will solve the next problem.

I have solved 9 problems.

I will solve the next problem.

I have solved 10 problems.

I will solve the next problem.

I have solved 11 problems.

I will solve the next problem.

I have solved 12 problems.

I will solve the next problem.

I have solved 13 problems.

I will solve the next problem.

I have solved 14 problems.

I will solve the next problem.

I have solved 15 problems.

I will solve the next problem.

I have solved 16 problems.

I will solve the next problem.

I have solved 17 problems.

I will solve the next problem.

I have solved 18 problems.

I will solve the next problem.

I have solved 19 problems.

I will solve the next problem.

I have solved 20 problems.

I will solve the next problem.

I have solved 21 problems.

I will solve the next problem.

I have solved 22 problems.

I will solve the next problem.

I have solved 23 problems.

=======
Suggestion 2

def main():
    A, B, K = map(int, input().split())
    if A <= K:
        K -= A
        A = 0
        if B <= K:
            B = 0
        else:
            B -= K
    else:
        A -= K
    print(A, B)

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())

    if A >= K:
        A -= K
    else:
        K -= A
        A = 0
        if B >= K:
            B -= K
        else:
            B = 0

    print(A, B)

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        A -= K
    elif A + B >= K:
        B -= K - A
        A = 0
    else:
        A = 0
        B = 0
    print(A, B)

=======
Suggestion 5

def main():
    a, b, k = map(int, input().split())
    if k <= a:
        a -= k
    else:
        k -= a
        a = 0
        b -= k
        if b < 0:
            b = 0
    print(a, b)

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        print(A-K, B)
    elif A + B >= K:
        print(0, A + B - K)
    else:
        print(0, 0)

=======
Suggestion 7

def main():
    A,B,K = map(int,input().split())
    if A >= K:
        A = A - K
    else:
        K = K - A
        A = 0
        if B >= K:
            B = B - K
        else:
            B = 0
    print(A,B)
    return

=======
Suggestion 8

def main():
    A, B, K = [int(n) for n in input().split()]
    if A >= K:
        A -= K
    else:
        K -= A
        A = 0
        if B >= K:
            B -= K
    print(A, B)

=======
Suggestion 9

def main():
    #input
    A, B, K = map(int, input().split())

    #compute
    if A >= K:
        A -= K
    else:
        K -= A
        A = 0
        if B >= K:
            B -= K
        else:
            B = 0

    #output
    print(A, B)

=======
Suggestion 10

def main():
    # Get input
    a, b, k = map(int, input().split())

    # If k is greater than the sum of a and b, then both of them will have 0 cookies
    if k >= a + b:
        print(0, 0)
    # If k is greater than a, then a will have 0 cookies, and b will have b - (k - a)
    elif k >= a:
        print(0, b - (k - a))
    # Otherwise, both of them will have a - k and b
    else:
        print(a - k, b)
