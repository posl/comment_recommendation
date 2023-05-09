Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a + b >= 15 and b >= 8:
        print(1)
    elif a + b >= 10 and b >= 3:
        print(2)
    elif a + b >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 2

def ice_cream_type(A, B):
    if A + B >= 15 and B >= 8:
        return 1
    elif A + B >= 10 and B >= 3:
        return 2
    elif A + B >= 3:
        return 3
    else:
        return 4

=======
Suggestion 3

def ice_cream():
    A, B = map(int, input().split())
    if A+B >= 15 and B >= 8:
        return 1
    elif A+B >= 10 and B >= 3:
        return 2
    elif A+B < 10 and A >= 3:
        return 3
    else:
        return 4

=======
Suggestion 4

def icecream():
    a, b = map(int, input().split())
    if a+b >= 15 and b >= 8:
        return 1
    if a+b >= 10 and b >= 3:
        return 2
    if a+b >= 3:
        return 3
    return 4

print(icecream())

=======
Suggestion 5

def icecream_or_ice_milk(a, b):
    if a + b >= 15 and b >= 8:
        return 1
    elif a + b >= 10 and b >= 3:
        return 2
    elif a + b >= 3:
        return 3
    else:
        return 4

=======
Suggestion 6

def ice_cream_or_ice_milk_or_lacto_ice_or_flavored_ice(a, b):
    if a + b < 15:
        return 4
    elif b >= 10:
        return 1
    elif b >= 3:
        return 2
    else:
        return 3
