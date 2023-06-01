Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,w = map(int, input().split())
    min = 0
    max = 0
    for i in range(1,1000):
        if a*i <= w*1000 <= b*i:
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
    a,b,w = map(int,input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(a,b+1):
        if w%i == 0:
            min = w//i
            break
    for i in range(b,a-1,-1):
        if w%i == 0:
            max = w//i
            break
    if min == 0 and max == 0:
        print('UNSATISFIABLE')
    else:
        print(min,max)

=======
Suggestion 3

def solve():
    a,b,w=map(int,input().split())
    w*=1000
    min=0
    max=0
    for i in range(1,w+1):
        if(a*i<=w and w<=b*i):
            if(min==0):
                min=i
            max=i
    if(min==0):
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 4

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    ans = [0, 0]
    for i in range(1, w+1):
        if a*i <= w and w <= b*i:
            ans[0] = i
            break
    for i in range(w, 0, -1):
        if a*i <= w and w <= b*i:
            ans[1] = i
            break
    if ans[0] == 0:
        print("UNSATISFIABLE")
    else:
        print(ans[0], ans[1])

=======
Suggestion 5

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = w // b
    max = w // a
    if min * a > w or max * b < w:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 6

def main():
    a,b,w=map(int,input().split())
    w*=1000
    min_num=w//b
    max_num=w//a
    if w%b==0:
        min_num=w//b
    else:
        min_num=w//b+1
    if w%a==0:
        max_num=w//a
    else:
        max_num=w//a
    if min_num>max_num:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)

=======
Suggestion 7

def main():
    # 读取输入
    a,b,w = map(int,input().split())
    # 由于题目要求输出最大最小，所以先把最小的橙子数量算出来
    min_num = w*1000//b
    # 由于题目要求输出最大最小，所以先把最大的橙子数量算出来
    max_num = w*1000//a
    # 如果最小的橙子数量乘以最小的重量大于总重量或者最大的橙子数量乘以最大的重量小于总重量，那么就不存在这样的橙子
    if min_num*a > w*1000 or max_num*b < w*1000:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)

=======
Suggestion 8

def main():
    a,b,w = map(int,input().split())
    w = w*1000
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

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    ans = []
    for i in range(1,w+1):
        if a*i <= w <= b*i:
            ans.append(i)
    if len(ans) == 0:
        print("UNSATISFIABLE")
    else:
        print(min(ans),max(ans))

=======
Suggestion 10

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(1,1001):
        if a*i <= w <= b*i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print('UNSATISFIABLE')
    else:
        print(min,max)
