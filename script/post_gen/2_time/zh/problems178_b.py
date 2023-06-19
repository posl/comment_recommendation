Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d = map(int,input().split())
    print(max(a*c,a*d,b*c,b*d))

=======
Suggestion 2

def f(a,b,c,d):
    if a*c > a*d:
        if a*c > b*c:
            if a*c > b*d:
                return a*c
            else:
                return b*d
        else:
            if b*c > b*d:
                return b*c
            else:
                return b*d
    else:
        if a*d > b*c:
            if a*d > b*d:
                return a*d
            else:
                return b*d
        else:
            if b*c > b*d:
                return b*c
            else:
                return b*d

=======
Suggestion 3

def maxProduct(a,b,c,d):
    if b < c or d < a:
        return -1
    else:
        return max(a*c, a*d, b*c, b*d)
