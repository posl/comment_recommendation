Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c, d = map(int, input().split())
    print(max(a*c, a*d, b*c, b*d))

=======
Suggestion 2

def main():
    a,b,c,d = map(int, input().split())
    l = [a*c, a*d, b*c, b*d]
    print(max(l))

main()

=======
Suggestion 3

def main():
    a,b,c,d = map(int,input().split())
    if b*c >= a*d:
        print(b*c)
    else:
        print(a*d)

=======
Suggestion 4

def main():
    #input
    a,b,c,d = map(int,input().split())
    #output
    print(max(a*c,a*d,b*c,b*d))

=======
Suggestion 5

def solve(a,b,c,d):
    if b*c > a*d:
        return b*c
    else:
        return a*d
