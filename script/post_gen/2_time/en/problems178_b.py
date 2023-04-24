Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c, d = map(int, input().split())
    print(max(a*c, a*d, b*c, b*d))

=======
Suggestion 2

def main():
    a, b, c, d = map(int, input().split())
    print(max(a*c, a*d, b*c, b*d))
main()

=======
Suggestion 3

def main():
    a,b,c,d = map(int,input().split())
    if b < 0 or d < 0:
        print(max(a*c,a*d,b*c,b*d))
    elif a > 0 or c > 0:
        print(max(a*c,a*d,b*c,b*d))
    else:
        print(max(a*c,b*d))

=======
Suggestion 4

def main():
    a,b,c,d = map(int,input().split())
    if a * d > b * c:
        print(a * d)
    else:
        print(b * c)

=======
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
    if a <= 0 and b >= 0:
        if c <= 0 and d >= 0:
            print(max(a*d,b*c))
        elif c > 0:
            print(b*c)
        elif d < 0:
            print(a*d)
    elif a > 0:
        print(b*c)
    elif b < 0:
        print(a*d)

=======
Suggestion 6

def maxProduct(a, b, c, d):
    if a <= 0 and b >= 0 and c <= 0 and d >= 0:
        return max(abs(a) * abs(c), abs(a) * abs(d), abs(b) * abs(c), abs(b) * abs(d))
    else:
        return max(a * c, a * d, b * c, b * d)

a, b, c, d = map(int, input().split())
print(maxProduct(a, b, c, d))
