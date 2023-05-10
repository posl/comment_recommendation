Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d = map(int,input().split())
    print(max(a*c,a*d,b*c,b*d))

=======
Suggestion 2

def main():
    a, b, c, d = map(int, input().split())
    print(max(max(a * c, a * d), max(b * c, b * d)))
