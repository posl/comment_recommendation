Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H = int(input())
    print((H*(12800000+H))**(1/2))

main()

=======
Suggestion 2

def main():
    H = int(input())
    print(((H * (12800000 + H)) ** 0.5))

=======
Suggestion 3

def main():
    H = int(input())
    print(((H*(12800000+H))**(1/2)))

=======
Suggestion 4

def main():
    import math
    H = int(input())
    print(math.sqrt(H*(12800000+H)))

=======
Suggestion 5

def main():
    from math import sqrt
    H = int(input())
    print(sqrt((H*(12800000+H))))

=======
Suggestion 6

def main():
    H = int(input())
    print(((12800000+H)*H)**(1/2))

main()

I made this program for a contest. I think it's correct, but the judge says it's wrong. I don't know why. Can someone explain to me what's wrong with it?

I think it's because of the floating point error. I tried to change the code like this:
