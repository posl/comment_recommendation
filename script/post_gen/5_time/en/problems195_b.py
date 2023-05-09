Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    if w % a == 0:
        min = w // a
    else:
        min = w // a + 1
    max = w // b
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 2

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min_count = 0
    max_count = 0
    for i in range(1, w+1):
        if a*i <= w and w <= b*i:
            min_count = i
            break
    for i in range(w, 0, -1):
        if a*i <= w and w <= b*i:
            max_count = i
            break
    if min_count == 0 or max_count == 0:
        print('UNSATISFIABLE')
    else:
        print(min_count, max_count)
    return

=======
Suggestion 3

def main():
    a,b,w = map(int, input().split())
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
        print(min, max)

=======
Suggestion 4

def solve(a, b, w):
    min_oranges = 0
    max_oranges = 0
    for i in range(1, 1001):
        if a*i <= w*1000 <= b*i:
            if min_oranges == 0:
                min_oranges = i
            max_oranges = i
    if min_oranges == 0:
        print("UNSATISFIABLE")
    else:
        print(min_oranges, max_oranges)

=======
Suggestion 5

def main():
    a,b,w = map(int, input().split())
    w *= 1000
    mn = 1000000000
    mx = 0
    for i in range(1, w+1):
        if a*i <= w and w <= b*i:
            mn = min(mn, i)
            mx = max(mx, i)
    if mn == 1000000000:
        print('UNSATISFIABLE')
    else:
        print(mn, mx)

=======
Suggestion 6

def main():
    a,b,w = map(int, input().split())
    w *= 1000
    min_count = 1000000
    max_count = 0
    for i in range(1,w+1):
        if a*i <= w and w <= b*i:
            min_count = min(min_count, i)
            max_count = max(max_count, i)
    if min_count == 1000000:
        print("UNSATISFIABLE")
    else:
        print(min_count, max_count)

=======
Suggestion 7

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = int(w/b)
    max = int(w/a)
    if w%b != 0:
        min += 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 8

def main():
    A,B,W = map(int,input().split())
    W = W * 1000
    min_num = 1000000
    max_num = -1
    for i in range(1,1000001):
        if A * i <= W and W <= B * i:
            min_num = min(min_num,i)
            max_num = max(max_num,i)
    if max_num == -1:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)

=======
Suggestion 9

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = int(W / B)
    max = int(W / A)
    if min == max:
        print(min, max)
    elif min < max:
        print(min, max)
    else:
        print("UNSATISFIABLE")

=======
Suggestion 10

def oranges(a,b,w):
    min_oranges = 0
    max_oranges = 0
    for i in range(w*1000):
        if (i+1)*a <= w*1000 and (i+1)*b >= w*1000:
            min_oranges = i+1
        if (i+1)*a > w*1000:
            break
    for i in range(w*1000):
        if (i+1)*b >= w*1000:
            max_oranges = i+1
            break
    if min_oranges == 0 and max_oranges == 0:
        print("UNSATISFIABLE")
    else:
        print(min_oranges,max_oranges)
