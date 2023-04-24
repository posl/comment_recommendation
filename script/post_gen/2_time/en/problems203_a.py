Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)

main()

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif a == c:
        print(b)
    else:
        print(0)

=======
Suggestion 4

def main():
    nums = input().split()
    nums = [int(x) for x in nums]
    if nums[0] == nums[1]:
        print(nums[2])
    elif nums[0] == nums[2]:
        print(nums[1])
    elif nums[1] == nums[2]:
        print(nums[0])
    else:
        print(0)

=======
Suggestion 5

def main():
    # read input
    a, b, c = map(int, input().split())

    # solve problem
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)

=======
Suggestion 6

def main():
    # Read three integers
    a, b, c = map(int, input().split())
    # If there are two same numbers among a, b, and c, print the remaining number. Otherwise, print 0.
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)
