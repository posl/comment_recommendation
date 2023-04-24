Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((N - 1) // min(A, B, C, D, E) + 5)

=======
Suggestion 2

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_num = min(A, B, C, D, E)
    ans = 5 + (N - 1) // min_num
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_time = min(A, B, C, D, E)
    print(-(-N // min_time) + 4)

=======
Suggestion 4

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(((N - 1) // min(A, B, C, D, E)) + 5)

=======
Suggestion 5

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_num = min(A,B,C,D,E)
    print(4 + (N-1+min_num-1)//min_num)

=======
Suggestion 6

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min = A
    if B < min:
        min = B
    if C < min:
        min = C
    if D < min:
        min = D
    if E < min:
        min = E
    print((N + min - 1) // min + 4)

=======
Suggestion 7

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(N, A, B, C, D, E)
    min = A
    if min > B:
        min = B
    if min > C:
        min = C
    if min > D:
        min = D
    if min > E:
        min = E
    #print(min)
    if N % min == 0:
        print(N // min + 4)
    else:
        print(N // min + 5)

=======
Suggestion 8

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    min_time = min(a,b,c,d,e)
    print((n-1)//min_time + 5)

=======
Suggestion 9

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    # Find the smallest of A, B, C, D and E
    # The smallest of A, B, C, D and E is the minimum time needed to reach City 6
    smallest = min(A, B, C, D, E)
    # If N is smaller than the smallest of A, B, C, D and E, the minimum time needed to reach City 6 is N
    if N <= smallest:
        print(N)
    # If N is not smaller than the smallest of A, B, C, D and E, the minimum time needed to reach City 6 is N//smallest + 4
    else:
        print(N//smallest + 4)

=======
Suggestion 10

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    # 1. Find the minimum time required for one person to reach City 6.
    min_time = min(A, B, C, D, E)

    # 2. Find the minimum number of vehicles required for N people to reach City 6.
    min_num = N // min_time
    if N % min_time != 0:
        min_num += 1

    # 3. Output the minimum time required for all of the people to reach City 6.
    print(min_num + 4)
