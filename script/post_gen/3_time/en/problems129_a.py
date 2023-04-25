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
    P, Q, R = map(int, input().split())
    print(min(P+Q, Q+R, R+P))

=======
Suggestion 3

def main():
    p, q, r = map(int, input().split())
    print(min(p+q, q+r, r+p))

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    print(min(a+b,b+c,c+a))
