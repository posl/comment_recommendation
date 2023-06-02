Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读入数据
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)

    # 计算路径长度
    import itertools
    sum = 0
    for perm in itertools.permutations(range(n)):
        for i in range(n-1):
            sum += ((x[perm[i]]-x[perm[i+1]])**2 + (y[perm[i]]-y[perm[i+1]])**2)**0.5

    # 输出结果
    print(sum / math.factorial(n))

=======
Suggestion 2

def get_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

=======
Suggestion 3

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 4

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    import itertools
    total = 0
    for i in itertools.permutations(range(N)):
        for j in range(N - 1):
            total += ((x[i[j]] - x[i[j + 1]]) ** 2 + (y[i[j]] - y[i[j + 1]]) ** 2) ** 0.5
    print(total / (N - 1))

=======
Suggestion 5

def getDistance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

=======
Suggestion 6

def get_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

=======
Suggestion 7

def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)
