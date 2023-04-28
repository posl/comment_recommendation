Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6 and A <= 12:
        print(int(B/2))
    else:
        print(0)


main()

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(b // 2)
    else:
        print(0)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(B//2)
    else:
        print(0)

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(b//2)
    else:
        print(0)

=======
Suggestion 5

def calc_fee(age, fee):
    if age >= 13:
        return fee
    elif age >= 6 and age <= 12:
        return int(fee / 2)
    else:
        return 0

=======
Suggestion 6

def solve():
    a,b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(int(b/2))
    else:
        print(0)
