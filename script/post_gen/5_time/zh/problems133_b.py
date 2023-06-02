Synthesizing 10/10 solutions

=======
Suggestion 1

def read_ints():
    return list(map(int, input().split()))

=======
Suggestion 2

def calDistance(x,y):
    import math
    sum = 0
    for i in range(len(x)):
        sum += (x[i]-y[i])**2
    return math.sqrt(sum)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    x = []
    for i in range(N):
        x.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            dis = 0
            for k in range(D):
                dis += (x[i][k] - x[j][k])**2
            if int(dis**0.5)**2 == dis:
                count += 1
    print(count)

=======
Suggestion 4

def get_distance(x, y):
    #计算两个点之间的距离
    distance = 0
    for i in range(len(x)):
        distance += (x[i] - y[i])**2
    return distance**0.5

=======
Suggestion 5

def distance(x, y):
    dist = 0
    for i in range(len(x)):
        dist += (x[i] - y[i]) ** 2
    return dist ** 0.5

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if distance(X[i], X[j]).is_integer():
            ans += 1
print(ans)

=======
Suggestion 6

def get_distance(a, b):
    distance = 0
    for i in range(len(a)):
        distance += (a[i] - b[i]) ** 2
    return distance ** 0.5

=======
Suggestion 7

def is_integer(num):
    if num == int(num):
        return True
    else:
        return False

N, D = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))

count = 0
for i in range(N):
    for j in range(i+1, N):
        distance = 0
        for k in range(D):
            distance += (X[i][k] - X[j][k])**2
        if is_integer(distance**0.5):
            count += 1

print(count)

=======
Suggestion 8

def distance(x,y):
    sum=0
    for i in range(len(x)):
        sum+=pow((x[i]-y[i]),2)
    return pow(sum,0.5)

n,d=map(int,input().split())
x=[]
for i in range(n):
    x.append(list(map(int,input().split())))
count=0
for i in range(n):
    for j in range(i+1,n):
        if distance(x[i],x[j]).is_integer():
            count+=1
print(count)

=======
Suggestion 9

def is_integer(num):
    if int(num) == num:
        return True
    else:
        return False

=======
Suggestion 10

def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = sum([(x[i][k]-x[j][k])**2 for k in range(d)])**0.5
            if dist.is_integer():
                cnt += 1
    print(cnt)
