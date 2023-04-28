Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(7 - a + 7 - b + 7 - c)

=======
Suggestion 2

def main():
    # input
    a, b, c = map(int, input().split())

    # compute

    # output
    print(7-a+7-b+7-c)

=======
Suggestion 3

def reverse_dice(num):
    return 7 - num


a, b, c = map(int, input().split())
print(reverse_dice(a) + reverse_dice(b) + reverse_dice(c))

=======
Suggestion 4

def reverse(a):
    return 7-a

a,b,c = map(int,input().split())
print(reverse(a)+reverse(b)+reverse(c))
