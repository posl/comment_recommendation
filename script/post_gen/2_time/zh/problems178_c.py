Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(a, b, c, d):
    return max(a*c, a*d, b*c, b*d)

=======
Suggestion 2

def main():
    a,b,c,d = map(int, input().split())
    print(max(a*c,a*d,b*c,b*d))

=======
Suggestion 3

def solution(a, b, c, d):
    result = 0
    for x in range(a, b + 1):
        for y in range(c, d + 1):
            result = max(result, x * y)
    return result

=======
Suggestion 4

def max_product(a,b,c,d):
    if a == 0 and b == 0 and c == 0 and d == 0:
        return 0
    elif a == 0 and b == 0:
        return c * d
    elif c == 0 and d == 0:
        return a * b
    elif a == 0:
        if c > 0:
            return c * b
        else:
            return d * b
    elif b == 0:
        if c > 0:
            return c * a
        else:
            return d * a
    elif c == 0:
        if a > 0:
            return a * d
        else:
            return b * d
    elif d == 0:
        if a > 0:
            return a * c
        else:
            return b * c
    else:
        if a > 0 and c > 0:
            return a * c
        elif a > 0 and d > 0:
            return a * d
        elif b > 0 and c > 0:
            return b * c
        elif b > 0 and d > 0:
            return b * d
        elif a < 0 and c < 0:
            return a * c
        elif a < 0 and d < 0:
            return a * d
        elif b < 0 and c < 0:
            return b * c
        elif b < 0 and d < 0:
            return b * d
        else:
            return a * d

=======
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
    print(max(a*c,a*d,b*c,b*d))
main()

=======
Suggestion 6

def max(a,b):
    if a>b:
        return a
    else:
        return b
