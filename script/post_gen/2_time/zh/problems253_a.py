Synthesizing 10/10 solutions

=======
Suggestion 1

def is_median(a,b,c):
    if a<b and b<c:
        return True
    elif c<b and b<a:
        return True
    else:
        return False

a,b,c = map(int,input().split())

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if a <= b <= c or c <= b <= a:
        print("是")
    else:
        print("没有")

=======
Suggestion 3

def median(a,b,c):
    if b >= a >= c or c >= a >= b:
        return "是"
    else:
        return "没有"
a,b,c = map(int,input().split())
print(median(a,b,c))

=======
Suggestion 4

def median(a,b,c):
    if a<=b<=c or c<=b<=a:
        print("是")
    else:
        print("没有")

a,b,c = map(int,input().split())
median(a,b,c)

=======
Suggestion 5

def is_middle(a,b,c):
    if (a <= b and a >= c) or (a >= b and a <= c):
        return True
    else:
        return False

=======
Suggestion 6

def median(a,b,c):
    if a <= b <= c or c <= b <= a:
        return True
    else:
        return False

a,b,c = map(int,input().split())

=======
Suggestion 7

def middle(a, b, c):
    if (b >= a and b <= c) or (b <= a and b >= c):
        return True
    else:
        return False

=======
Suggestion 8

def main():
    numbers = input().split()
    numbers = [int(s) for s in numbers]
    numbers.sort()
    if numbers[1] == numbers[0] + numbers[2] - numbers[1]:
        print('是')
    else:
        print('否')

=======
Suggestion 9

def mid(a,b,c):
    if a <= b <= c or c <= b <= a:
        return True
    else:
        return False

a,b,c = map(int,input().split())

=======
Suggestion 10

def main():
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if (b >= a and b <= c) or (b <= a and b >= c):
        print("Yes")
    else:
        print("No")
