Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,w = map(int,input().split())
    w = w*1000
    min = 0
    max = 0
    for i in range(1,w+1):
        if a*i <= w <= b*i:
            min = i
            break
    for i in range(w,0,-1):
        if a*i <= w <= b*i:
            max = i
            break
    if min == 0 and max == 0:
        print('UNSATISFIABLE')
    else:
        print(min,max)

=======
Suggestion 2

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = 0
    max = 0
    for i in range(1, 1000001):
        if A <= W / i <= B:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 3

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(1, w + 1):
        if a <= i <= b:
            if w % i == 0:
                min = i
                max = i
            elif w % i != 0:
                if min == 0:
                    min = i
                max = i
    if min == 0 and max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 4

def main():
    a,b,w = map(int, input().split())
    w = w * 1000
    min = 1000000
    max = 0
    for i in range(1, w+1):
        if a <= i and i <= b:
            if w % i == 0:
                if min > w // i:
                    min = w // i
                if max < w // i:
                    max = w // i
    if max == 0:
        print("UNSATISFIABLE")
    else:
        print(str(min) + " " + str(max))

=======
Suggestion 5

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 1000000
    max = 0
    for i in range(w//b+1,w//a+1):
        if a*i <= w and w <= b*i:
            if i < min:
                min = i
            if i > max:
                max = i
    if min == 1000000:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 6

def main():
    a,b,w = map(int,input().split())
    min = 0
    max = 0
    for i in range(1,1001):
        if a*i <= w*1000 and w*1000 <= b*i:
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
    a,b,w=map(int,input().split())
    w*=1000
    min_num,max_num=0,0
    for i in range(1,w+1):
        if a*i<=w and w<=b*i:
            if min_num==0:
                min_num=i
            max_num=i
    if min_num==0:
        print('UNSATISFIABLE')
    else:
        print(min_num,max_num)

=======
Suggestion 8

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 1000000
    max = 0
    for i in range(1,w+1):
        if a <= i <= b:
            if min > i:
                min = i
            if max < i:
                max = i
    if min == 1000000:
        print('UNSATISFIABLE')
    else:
        print(min//1000,max//1000)

=======
Suggestion 9

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min_num = w//b
    max_num = w//a
    if w%a != 0:
        min_num += 1
    if min_num > max_num:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)

=======
Suggestion 10

def main():
    A,B,W = map(int, input().split())
    W = W * 1000
    min = 0
    max = 0
    if W % A == 0:
        min = W // A
    else:
        min = W // A + 1
    if W % B == 0:
        max = W // B
    else:
        max = W // B
    if min > max:
        print('UNSATISFIABLE')
    else:
        print(min, max)
