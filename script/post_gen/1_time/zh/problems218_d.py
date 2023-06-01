Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def count_rectangles(n, points):
    count = 0
    x = [0 for i in range(n)]
    y = [0 for i in range(n)]
    for i in range(n):
        x[i] = points[i][0]
        y[i] = points[i][1]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if x[i] < x[j] and y[i] < y[j]:
                if [x[i], y[j]] in points and [x[j], y[i]] in points:
                    count += 1
    return count

=======
Suggestion 3

def get_input():
    n = int(raw_input())
    points = []
    for i in range(n):
        x, y = map(int, raw_input().split())
        points.append((x, y))
    return points

=======
Suggestion 4

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = input().split()
        x.append(int(a))
        y.append(int(b))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if x[i] != x[j] and y[i] != y[j]:
                if x[i] in x and y[j] in y:
                    count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x.append(int(input().split()[0]))
        y.append(int(input().split()[1]))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] != x[j] and y[i] != y[j]:
                if x[i] in x and y[j] in y:
                    ans += 1
    print(ans)
    return

=======
Suggestion 6

def get_input():
    n = int(input())
    x = []
    y = []
    for i in range(0,n):
        line = input()
        x.append(int(line.split(" ")[0]))
        y.append(int(line.split(" ")[1]))
    return n,x,y

=======
Suggestion 7

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1,y1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j]:
                continue
            for k in range(j+1,n):
                if y[i] == y[k]:
                    continue
                if x[k] == x[j]:
                    continue
                for l in range(k+1,n):
                    if y[k] == y[l]:
                        continue
                    if x[l] == x[i]:
                        continue
                    if y[i] == y[j]:
                        continue
                    if x[l] == x[k]:
                        continue
                    if y[j] == y[l]:
                        continue
                    ans += 1
    print(ans)

=======
Suggestion 8

def get_point():
    N = int(input())
    points = []
    for i in range(N):
        points.append(tuple(map(int, input().split())))
    return N, points
