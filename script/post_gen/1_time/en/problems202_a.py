Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(21 - a - b - c)

=======
Suggestion 2

def main():
    # input
    a, b, c = map(int, input().split())

    # compute

    # output
    print(21 - a - b - c)

=======
Suggestion 3

def dice(a,b,c):
    if (a >= 1 and a <= 6) and (b >= 1 and b <= 6) and (c >= 1 and c <= 6):
        return (7 - a) + (7 - b) + (7 - c)
    else:
        return False

=======
Suggestion 4

def solve():
    a,b,c = map(int,input().split())
    print(7-a+7-b+7-c)

=======
Suggestion 5

def dice_sum(a,b,c):
    sum = 0
    sum = 7 - a + 7 - b + 7 - c
    return sum

=======
Suggestion 6

def dice_sum():
    dice = list(map(int, input().split()))
    print(21 - sum(dice))

dice_sum()

=======
Suggestion 7

def dice_sum(a,b,c):
    return 21-(a+b+c)
