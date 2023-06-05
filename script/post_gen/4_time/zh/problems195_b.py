Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = (w//b) if w%b==0 else (w//b)+1
    max = w//a
    if min>max:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 2

def get_input():
    input_list = input().split()
    return input_list

=======
Suggestion 3

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 1000000000
    max = 0
    for i in range(1,1000001):
        if a*i <= w <= b*i:
            if i < min:
                min = i
            if i > max:
                max = i
    if min == 1000000000:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 4

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = w // b
    if w % b != 0:
        min += 1
    max = w // a
    if w % a != 0:
        max += 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 5

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = w // b
    max = w // a
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 6

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min_num = 1000000
    max_num = 0
    for i in range(a,b+1):
        if i * w % 1000 == 0:
            min_num = min(min_num,i * w // 1000)
            max_num = max(max_num,i * w // 1000)
    if min_num == 1000000:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)

=======
Suggestion 7

def main():
    a,b,w = map(int,input().split())
    ans = []
    for i in range(1,1001):
        if a*i <= w*1000 <= b*i:
            ans.append(i)
    if len(ans) == 0:
        print("UNSATISFIABLE")
    else:
        print(min(ans),max(ans))

=======
Suggestion 8

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
        print('UNSATISFIABLE')
    else:
        print(min,max)

=======
Suggestion 9

def count_orange(a,b,w):
    min = 0
    max = 0
    if w%a == 0:
        min = w//a
    else:
        min = w//a + 1
    if w%b == 0:
        max = w//b
    else:
        max = w//b
    if max < min:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 10

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 1000000
    max = 0
    for i in range(a,b+1):
        if i <= w and w <= i*b:
            if i < min:
                min = i
            if i > max:
                max = i
    if min == 1000000:
        print("UNSATISFIABLE")
    else:
        print(min,max)
