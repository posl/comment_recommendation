Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    # compute

    # output
    print((N + min(A, B, C, D, E) - 1) // min(A, B, C, D, E) + 4)

=======
Suggestion 2

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(5 + (N - 1) // min(A, B, C, D, E))

=======
Suggestion 3

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(5 + (N - 1) // min([A, B, C, D, E]))

=======
Suggestion 4

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_people = min(A,B,C,D,E)
    if N % min_people == 0:
        print(int(N/min_people) + 4)
    else:
        print(int(N/min_people) + 5)

=======
Suggestion 5

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(5 + (n-1)//min(a, b, c, d, e))

=======
Suggestion 6

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    
    print(5+((n-1)//min(a,b,c,d,e))+1)
    
main()

=======
Suggestion 7

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    #print(N,A,B,C,D,E)
    #print(N//min(A,B,C,D,E) + 5)
    #print(N//min(A,B,C,D,E) + 5 if N%min(A,B,C,D,E) == 0 else N//min(A,B,C,D,E) + 6)
    print(N//min(A,B,C,D,E) + 5 if N%min(A,B,C,D,E) == 0 else N//min(A,B,C,D,E) + 6)

=======
Suggestion 8

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    
    print(int(n/min(a,b,c,d,e)) + (5 if n%min(a,b,c,d,e) else 0) + 4)

=======
Suggestion 9

def main():
    import sys
    import math
    #from collections import defaultdict
    #from collections import deque
    #import heapq
    #from fractions import gcd
    #from collections import Counter
    #from itertools import combinations
    
    #input = sys.stdin.readline
    
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    
    print(math.ceil(N/min(A,B,C,D,E))+4)
