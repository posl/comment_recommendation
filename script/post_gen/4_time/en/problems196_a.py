Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a-c, a-d, b-c, b-d))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(b - c)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a-c, b-d))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b - c, d - a))

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    print(max((a-c),(a-d),(b-c),(b-d)))

=======
Suggestion 6

def max_diff(a,b,c,d):
    return max(a*c,a*d,b*c,b*d)

a,b = map(int, input().split())
c,d = map(int, input().split())
print(max_diff(a,b,c,d))
