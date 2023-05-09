Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pqr = input().split()
    p = int(pqr[0])
    q = int(pqr[1])
    r = int(pqr[2])

    print(min(p+q, q+r, r+p))

=======
Suggestion 2

def main():
    p, q, r = map(int, input().split())
    print(min(p+q, q+r, r+p))

=======
Suggestion 3

def main():
    P, Q, R = map(int, input().split())
    print(min(P + Q, Q + R, R + P))

=======
Suggestion 4

def problems129_a():
    p,q,r = map(int, input().split())
    print(min(p+q, q+r, r+p))

=======
Suggestion 5

def solve():
    p,q,r = map(int,input().split())
    print(min(p+q,q+r,r+p))

=======
Suggestion 6

def main():
    #input
    P,Q,R = map(int,input().split())
    #compute
    result = P+Q+R-max(P,Q,R)
    #output
    print(result)

=======
Suggestion 7

def solve(P,Q,R):
    return min(P+Q,Q+R,R+P)

=======
Suggestion 8

def solution(P, Q, R):
    print(min(P+Q, Q+R, R+P))
