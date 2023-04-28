Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    max_num = 0
    min_num = 0
    for i in range(1, w + 1):
        if a * i <= w and w <= b * i:
            if max_num == 0:
                max_num = i
            min_num = i
    if min_num == 0:
        print("UNSATISFIABLE")
    else:
        print(min_num, max_num)

=======
Suggestion 2

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 1000000
    max = 0
    for i in range(1,w+1):
        if a*i <= w and b*i >=w:
            if i < min:
                min = i
            if i > max:
                max = i
    if min == 1000000:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 3

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = 0
    max = 0

    for i in range(1, w+1):
        if a * i <= w and w <= b * i:
            if min == 0:
                min = i
            max = i

    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 4

def main():
    a,b,w = map(int, input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(1,1001):
        if a*i <= w <= b*i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 5

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    max = 0
    min = 1000000000
    for i in range(1, w + 1):
        if a * i <= w and w <= b * i:
            if i > max:
                max = i
            if i < min:
                min = i
    if max == 0:
        print('UNSATISFIABLE')
    else:
        print(min, max)

=======
Suggestion 6

def main():
    a,b,w = map(int, input().split())
    w *= 1000
    min = 10000000
    max = 0
    for i in range(1, 1000001):
        if a * i <= w <= b * i:
            if min > i:
                min = i
            if max < i:
                max = i
    if max == 0:
        print('UNSATISFIABLE')
    else:
        print(min, max)

=======
Suggestion 7

def main():
    A, B, W = map(int, input().split())

    max = int(W * 1000 / A)
    min = int(W * 1000 / B)
    if min == max:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 8

def main():
    a,b,w = map(int,input().split())
    w = w * 1000
    if w%b == 0:
        min = w//b
    else:
        min = w//b + 1
    max = w//a
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 9

def solve():
    a,b,w = map(int, input().split())
    w *= 1000
    min = 1000000000
    max = 0
    for i in range(1,1000001):
        if a <= w / i and w / i <= b:
            if min > i:
                min = i
            if max < i:
                max = i
    if max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 10

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(1,w//a+1):
        if w == a*i:
            if min == 0:
                min = i
            max = i
        if a*i < w and w <= b*i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)
