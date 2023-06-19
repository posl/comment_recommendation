Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,w = map(int,input().split())
    w = w*1000
    # print(a,b,w)
    min = 0
    max = 0
    for i in range(1,w+1):
        # print(i)
        if a*i <= w and w <= b*i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 2

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = -1
    max = 0
    for i in range(1, W+1):
        if A * i <= W and W <= B * i:
            if min == -1:
                min = i
            max = i
    if min == -1:
        print('UNSATISFIABLE')
    else:
        print(min, max)

=======
Suggestion 3

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    max = 0
    min = 0
    for i in range(1,w+1):
        if a*i <= w <= b*i:
            min = i
            break
    for i in range(w,0,-1):
        if a*i <= w <= b*i:
            max = i
            break
    if max == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 4

def main():
    a,b,w = map(int,input().split())
    w = w*1000
    min_num = 0
    max_num = 0
    for i in range(a,b+1):
        if w%i==0:
            min_num = w//i
            break
    for i in range(b,a-1,-1):
        if w%i==0:
            max_num = w//i
            break
    if min_num==0 or max_num==0:
        print('UNSATISFIABLE')
    else:
        print(min_num,max_num)

=======
Suggestion 5

def main():
    a,b,w = map(int, input().split())
    w *= 1000
    if w%a == 0:
        min = w//a
    else:
        min = w//a + 1
    if w%b == 0:
        max = w//b
    else:
        max = w//b
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 6

def get_orange_num(A,B,W):
    min_num = -1
    max_num = -1
    for i in range(A,B+1):
        if i*1000//B == W:
            if min_num == -1:
                min_num = i
            max_num = i
        if i*1000//A == W:
            if max_num == -1:
                max_num = i
            min_num = i
    return min_num,max_num

=======
Suggestion 7

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min_num = w // b
    max_num = w // a
    if min_num > max_num:
        print('UNSATISFIABLE')
    else:
        print(min_num, max_num)

=======
Suggestion 8

def get_num():
    a,b,w = map(int,input().split())
    min_num = 0
    max_num = 0
    for i in range(1,1001):
        if a*i <= 1000*w <= b*i:
            min_num = i
            break
    for i in range(1,1001):
        if a*i <= 1000*w <= b*i:
            max_num = i
    if min_num == 0:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)

get_num()

=======
Suggestion 9

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = (w//b) if w%b == 0 else (w//b)+1
    max = w//a
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 10

def solve():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 1000000
    max = 0
    for i in range(a,b+1):
        if w % i == 0:
            if w // i <= max:
                max = w // i
            if w // i >= min:
                min = w // i
    if min == 1000000 or max == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)
