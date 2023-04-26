Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c, d = map(int, input().split())
    print(max(a*c, a*d, b*c, b*d))

=======
Suggestion 2

def main():
    a,b,c,d = map(int,input().split())
    if a >= 0 and c >= 0:
        print(a*d)
    elif a >= 0 and d <= 0:
        print(a*c)
    elif b <= 0 and c >= 0:
        print(b*d)
    elif b <= 0 and d <= 0:
        print(b*c)
    else:
        print(max(a*c,a*d,b*c,b*d))

=======
Suggestion 3

def main():
    a,b,c,d = map(int,input().split())
    if a > 0 and c > 0:
        print(max(a*c, a*d, b*c, b*d))
    elif a > 0 and d < 0:
        print(max(a*c, a*d, b*c, b*d))
    elif b < 0 and c > 0:
        print(max(a*c, a*d, b*c, b*d))
    elif b < 0 and d < 0:
        print(max(a*c, a*d, b*c, b*d))
    elif a > 0 and c <= 0 and d >= 0:
        print(max(a*c, a*d, b*c, b*d))
    elif b < 0 and c <= 0 and d >= 0:
        print(max(a*c, a*d, b*c, b*d))
    elif c > 0 and a <= 0 and b >= 0:
        print(max(a*c, a*d, b*c, b*d))
    elif d < 0 and a <= 0 and b >= 0:
        print(max(a*c, a*d, b*c, b*d))
    elif a <= 0 and b >= 0 and c <= 0 and d >= 0:
        print(max(a*c, a*d, b*c, b*d))
    else:
        print("Error")

=======
Suggestion 4

def main():
    a,b,c,d = map(int, input().split())
    if 0 <= a or 0 <= c:
        print(max(a*c, a*d, b*c, b*d))
    else:
        print(max(a*d, b*c))
