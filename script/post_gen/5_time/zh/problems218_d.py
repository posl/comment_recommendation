Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x.append(int(input().split()[0]))
        y.append(int(input().split()[1]))
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            if x[i] < x[j] and y[i] < y[j]:
                if x[i] in x[j:] and y[i] in y[j:]:
                    ans += 1
            elif x[i] > x[j] and y[i] > y[j]:
                if x[j] in x[i:] and y[j] in y[i:]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        tmp = input().split()
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if x[i] == x[j] or y[i] == y[j]:
                for k in range(j+1,N):
                    if x[i] == x[j] and x[j] == x[k]:
                        for l in range(k+1,N):
                            if y[i] == y[k] and y[j] == y[l]:
                                ans += 1
                    elif y[i] == y[j] and y[j] == y[k]:
                        for l in range(k+1,N):
                            if x[i] == x[k] and x[j] == x[l]:
                                ans += 1
    print(ans)

=======
Suggestion 4

def get_rect_num(x, y):
    rect_num = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            if (x[i], y[j]) in point_set and (x[j], y[i]) in point_set:
                rect_num += 1
    return rect_num

=======
Suggestion 5

def solve():
    pass

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            if x[i] in x[j] and y[i] in y[j]:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    return 0

=======
Suggestion 8

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1,y1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            if x[i] in x and y[j] in y:
                ans += 1
    print(ans)
