Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = W // B
    if W % B != 0:
        min += 1
    max = W // A
    if W % A != 0:
        max += 1
    if min > max:
        print('UNSATISFIABLE')
    else:
        print(min, max)

=======
Suggestion 2

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(1, w + 1):
        if a * i <= w and w <= b * i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print('UNSATISFIABLE')
    else:
        print(min, max)

=======
Suggestion 3

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = 1000000
    max = 0
    for i in range(1, w+1):
        if a*i <= w and w <= b*i:
            if i < min:
                min = i
            if i > max:
                max = i
    if max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 4

def main():
    A, B, W = map(int, input().split())
    W = W * 1000
    min = (W // B) + 1
    max = W // A
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 5

def main():
    a,b,w = map(int, input().split())
    w *= 1000
    min = 1000000
    max = 0
    for i in range(1,1000001):
        if a*i <= w and w <= b*i:
            if min > i:
                min = i
            if max < i:
                max = i
    if max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 6

def main():
    a,b,w = map(int, input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(1, 1000001):
        if a*i <= w <= b*i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 7

def main():
    A, B, W = map(int, input().split())

    min = 0
    max = 0

    if W * 1000 % B == 0:
        max = W * 1000 // B
    else:
        max = W * 1000 // B + 1

    if W * 1000 % A == 0:
        min = W * 1000 // A
    else:
        min = W * 1000 // A + 1

    if min > max:
        print('UNSATISFIABLE')
    else:
        print(min, max)

=======
Suggestion 8

def main():
    a,b,w = map(int, input().split())
    w *= 1000
    min_ = float('inf')
    max_ = 0
    for i in range(1,w+1):
        if a*i <= w <= b*i:
            min_ = min(min_,i)
            max_ = max(max_,i)
    if min_ == float('inf'):
        print('UNSATISFIABLE')
    else:
        print(min_,max_)

=======
Suggestion 9

def get_min_max_oranges(A, B, W):
    min_oranges = 0
    max_oranges = 0
    for i in range(1, W*1000+1):
        if A <= (W*1000)/i <= B:
            if min_oranges == 0:
                min_oranges = i
            max_oranges = i
    return min_oranges, max_oranges

=======
Suggestion 10

def get_input():
    return map(int, input().split())
