Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = 1000000
    max = 0
    for i in range(1, W+1):
        if A*i <= W and W <= B*i:
            if i <= min:
                min = i
            if i >= max:
                max = i
    if min == 1000000 or max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 2

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    max_n = 0
    min_n = 1000000
    for i in range(1, 1000001):
        if A*i <= W <= B*i:
            max_n = max(max_n, i)
            min_n = min(min_n, i)

    if max_n == 0:
        print("UNSATISFIABLE")
    else:
        print(min_n, max_n)

=======
Suggestion 3

def main():
    A,B,W = map(int,input().split())
    W = W * 1000
    ans = []
    for i in range(1,1001):
        if A * i <= W and W <= B * i:
            ans.append(i)
    if len(ans) == 0:
        print("UNSATISFIABLE")
    else:
        print(min(ans),max(ans))

=======
Suggestion 4

def resolve():
    import math
    a,b,w = map(int, input().split())
    w = w * 1000
    max = math.floor(w/a)
    min = math.ceil(w/b)
    if max < min:
        print("UNSATISFIABLE")
    else:
        print(min,max)
    return

=======
Suggestion 5

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    max = 0
    min = 0
    for i in range(1, w+1):
        if a <= w/i <= b:
            if min == 0:
                min = i
            max = i
    if max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 6

def main():
    a,b,w = map(int,input().split())

    w *= 1000

    min = 0
    max = 0
    for i in range(1,1000001):
        if a*i <= w and w <= b*i:
            if min == 0:
                min = i
            max = i

    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 7

def main():
    a,b,w = map(int,input().split())
    w = w*1000
    min = 0
    max = 0
    for i in range(1,1000000):
        if a*i <= w and w <= b*i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 8

def main():
    a,b,w = map(int, input().split())
    w *= 1000
    min_num = 0
    max_num = 0
    for i in range(1,1000001):
        if a*i <= w and w <= b*i:
            if min_num == 0:
                min_num = i
            max_num = i
    if min_num == 0:
        print('UNSATISFIABLE')
    else:
        print(min_num, max_num)

=======
Suggestion 9

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(1, 1000001):
        if a * i <= w and w <= b * i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print('UNSATISFIABLE')
    else:
        print('{} {}'.format(min, max))

=======
Suggestion 10

def main():
    A, B, W = map(int, input().split())
    W = W * 1000
    min = 0
    max = 0
    for i in range(1, 1001):
        if A * i <= W <= B * i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)
