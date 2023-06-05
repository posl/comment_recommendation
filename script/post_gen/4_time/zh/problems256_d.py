Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort()
    l = lr[0][0]
    r = lr[0][1]
    ans = []
    for i in range(1, n):
        if r < lr[i][0]:
            ans.append([l, r])
            l = lr[i][0]
            r = lr[i][1]
        else:
            r = max(r, lr[i][1])
    ans.append([l, r])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 2

def get_input():
    N = int(input())
    l = []
    for i in range(N):
        l.append(list(map(int, input().split())))
    return N, l

=======
Suggestion 3

def main():
    n = int(input())
    lrs = []
    for i in range(n):
        lrs.append(list(map(int, input().split())))
    lrs.sort(key=lambda x: x[0])
    ans = []
    ans.append(lrs[0])
    for i in range(1, n):
        if lrs[i][0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], lrs[i][1])
        else:
            ans.append(lrs[i])
    for i in ans:
        print(i[0], i[1])

=======
Suggestion 4

def main():
    n = int(input())
    interval = []
    for i in range(n):
        interval.append([int(i) for i in input().split()])
    interval.sort(key=lambda x:x[0])

    stack = [interval[0]]
    for i in range(1,n):
        if stack[-1][1] >= interval[i][0]:
            stack[-1][1] = max(stack[-1][1],interval[i][1])
        else:
            stack.append(interval[i])
    for s in stack:
        print(s[0],s[1])

=======
Suggestion 5

def main():
    n = int(input())
    lr_list = []
    for i in range(n):
        lr_list.append(list(map(int, input().split())))

    lr_list.sort(key=lambda x: x[0])
    x = lr_list[0][0]
    y = lr_list[0][1]
    for i in range(1, n):
        if lr_list[i][0] > y:
            print(x, y)
            x = lr_list[i][0]
            y = lr_list[i][1]
        elif lr_list[i][1] > y:
            y = lr_list[i][1]
    print(x, y)

=======
Suggestion 6

def solve():
    n = int(input())
    LR = []
    for i in range(n):
        LR.append(list(map(int,input().split())))
    LR.sort(key=lambda x:x[0])
    ans = []
    ans.append(LR[0][0])
    ans.append(LR[0][1])
    for i in range(1,n):
        if LR[i][0] <= ans[-1] and ans[-1] < LR[i][1]:
            ans[-1] = LR[i][1]
        elif LR[i][0] > ans[-1]:
            ans.append(LR[i][0])
            ans.append(LR[i][1])
    for i in range(0,len(ans),2):
        print(ans[i],ans[i+1])

=======
Suggestion 7

def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    l.sort()
    r.sort()
    print(l[0], r[-1])

=======
Suggestion 8

def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(L, R)
    print(L[0], R[-1])

=======
Suggestion 9

def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    data.sort(key=lambda x:x[0])
    new_data = [data[0]]
    for i in range(1, n):
        if new_data[-1][1] < data[i][0]:
            new_data.append(data[i])
        elif new_data[-1][1] < data[i][1]:
            new_data[-1][1] = data[i][1]
    for i in range(len(new_data)):
        print(new_data[i][0], new_data[i][1])

=======
Suggestion 10

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    left = l[0][0]
    right = l[0][1]
    for i in range(1, n):
        if l[i][0] <= right:
            right = max(right, l[i][1])
        else:
            print(left, right)
            left = l[i][0]
            right = l[i][1]
    print(left, right)
