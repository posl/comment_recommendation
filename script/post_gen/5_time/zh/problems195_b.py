Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = w // b
    max = w // a
    if min == max:
        if w % min == 0:
            print(min, max)
        else:
            print("UNSATISFIABLE")
    else:
        if w % min == 0 and w % max == 0:
            print(min, max)
        elif w % min == 0:
            print(min, max)
        elif w % max == 0:
            print(min, max)
        else:
            print("UNSATISFIABLE")

=======
Suggestion 2

def main():
    a,b,w=map(int,input().split())
    w=w*1000
    min=w//b
    max=w//a
    if w%a==0:
        if w//a==w//b:
            print(w//a,w//a)
        elif w//a!=w//b:
            print(w//a,w//b)
    else:
        if w//a==w//b:
            print('UNSATISFIABLE')
        elif w//a!=w//b:
            print(w//a+1,w//b)

=======
Suggestion 3

def main():
    a,b,w = map(int,input().split())
    min_num = 0
    max_num = 0
    if a > w*1000//b:
        print("UNSATISFIABLE")
    else:
        for i in range(1,w*1000//a+1):
            if a*i <= w*1000 and w*1000 <= b*i:
                if min_num == 0:
                    min_num = i
                max_num = i
        print(min_num,max_num)
    return

=======
Suggestion 4

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min_num = 0
    max_num = 0
    for i in range(a,b+1):
        if w % i == 0:
            max_num = w // i
            break
    for i in range(b,a-1,-1):
        if w % i == 0:
            min_num = w // i
            break
    if min_num == 0 and max_num == 0:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)

=======
Suggestion 5

def main():
    a,b,w=map(int,input().split())
    w=w*1000
    min_num=0
    max_num=0
    for i in range(a,b+1):
        if w%i==0:
            if min_num==0:
                min_num=w//i
            max_num=w//i
    if min_num==0:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)

=======
Suggestion 6

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    max_num = int(w / a)
    min_num = int(w / b)
    if min_num > max_num:
        print('UNSATISFIABLE')
    else:
        print(min_num, max_num)

=======
Suggestion 7

def solve():
    a,b,w=map(int,input().split())
    w*=1000
    ans_min=0
    ans_max=0
    for i in range(1,1000000):
        if a*i<=w and w<=b*i:
            ans_min=i
            break
    for i in range(1,1000000):
        if a*i>w or w>b*i:
            ans_max=i-1
            break
    if ans_min==0 and ans_max==0:
        print("UNSATISFIABLE")
    else:
        print(ans_min,ans_max)

=======
Suggestion 8

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(1,1001):
        if a*i <= w and w <= b*i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 9

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(a, b+1):
        if w % i == 0:
            if min == 0:
                min = w // i
            max = w // i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 10

def get_orange_num(a, b, w):
    min_num = 0
    max_num = 0
    if a > w or w > b:
        return 'UNSATISFIABLE'
    #最小值
    if w % a == 0:
        min_num = w // a
    else:
        min_num = w // a + 1
    #最大值
    max_num = w // b
    return str(min_num) + ' ' + str(max_num)
