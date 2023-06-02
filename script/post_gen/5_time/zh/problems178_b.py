Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def max_product(a,b,c,d):
    if a*c > a*d:
        if a*c > b*c:
            return a*c
        else:
            return b*c
    else:
        if a*d > b*d:
            return a*d
        else:
            return b*d

=======
Suggestion 2

def main():
    a,b,c,d = map(int,input().split())
    print(max(a*c,a*d,b*c,b*d))

=======
Suggestion 3

def get_max(a, b, c, d):
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
Suggestion 4

def main():
    a,b,c,d = map(int,input().split())
    print(max(a*c,a*d,b*c,b*d))
    return 0

=======
Suggestion 5

def main():
    a, b, c, d = map(int, input().split())
    x = [a, b]
    y = [c, d]
    print(max([i * j for i in x for j in y]))

=======
Suggestion 6

def max_product(a,b,c,d):
    if a*c>=a*d and a*c>=b*c and a*c>=b*d:
        return a*c
    elif a*d>=a*c and a*d>=b*c and a*d>=b*d:
        return a*d
    elif b*c>=a*c and b*c>=a*d and b*c>=b*d:
        return b*c
    else:
        return b*d
