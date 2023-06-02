Synthesizing 10/10 solutions

=======
Suggestion 1

def sort_by_better(x):
    return x[0]

=======
Suggestion 2

def get_max_value(n, m, cakes):
    cakes.sort(key=lambda x: x[0]-x[1]-x[2], reverse=True)
    result = 0
    for i in range(m):
        result += cakes[i][0]
    for i in range(m, n):
        result -= cakes[i][1]
    return result

=======
Suggestion 3

def get_max_value(n, m, cakes):
    cakes.sort(key=lambda x: x[0] + x[1] + x[2])
    cakes.reverse()
    max_value = 0
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if i + j + k > m:
                    break
                value = abs(cakes[i][0]) + abs(cakes[j][1]) + abs(cakes[k][2])
                if value > max_value:
                    max_value = value
    return max_value

=======
Suggestion 4

def main():
    n,m=map(int,input().split())
    x=[]
    y=[]
    z=[]
    for i in range(n):
        a,b,c=map(int,input().split())
        x.append(a)
        y.append(b)
        z.append(c)
    ans=0
    for i in range(2**3):
        k=[]
        for j in range(n):
            k.append(x[j]*(-1)**((i>>0)&1)+y[j]*(-1)**((i>>1)&1)+z[j]*(-1)**((i>>2)&1))
        k.sort(reverse=True)
        ans=max(ans,sum(k[:m]))
    print(ans)

=======
Suggestion 5

def get_max_value(n,m,beauty,delicious,popularity):
    max_value = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                value = abs(beauty[i])+abs(beauty[j])+abs(beauty[k])+abs(delicious[i])+abs(delicious[j])+abs(delicious[k])+abs(popularity[i])+abs(popularity[j])+abs(popularity[k])
                if value > max_value:
                    max_value = value
    return max_value

=======
Suggestion 6

def main():
    n,m = input().split()
    n = int(n)
    m = int(m)
    cakes = []
    for i in range(n):
        cakes.append(list(map(int,input().split())))
    cakes.sort(key=lambda x:abs(x[0])+abs(x[1])+abs(x[2]),reverse=True)
    ans = 0
    for i in range(m):
        ans += abs(cakes[i][0]) + abs(cakes[i][1]) + abs(cakes[i][2])
    print(ans)

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    cake = []
    for i in range(N):
        cake.append(list(map(int,input().split())))
    if N == 1:
        print(abs(cake[0][0]) + abs(cake[0][1]) + abs(cake[0][2]))
        return
    if M == 0:
        print(0)
        return
    if M == 1:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 2:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 3:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 4:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 5:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 6:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 7:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 8:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 9:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return

=======
Suggestion 8

def solve():
    n, m = map(int, input().split())
    x, y, z = [], [], []
    for i in range(n):
        xi, yi, zi = map(int, input().split())
        x.append(xi)
        y.append(yi)
        z.append(zi)
    ans = 0
    for i in range(2 ** 3):
        d = []
        for j in range(n):
            d.append(x[j] * ((i >> 0) & 1) + y[j] * ((i >> 1) & 1) + z[j] * ((i >> 2) & 1))
        d.sort(reverse=True)
        ans = max(ans, sum(d[:m]))
    print(ans)

solve()

=======
Suggestion 9

def main():
    # 输入
    N, M = map(int, input().split())
    # 蛋糕的美丽度、美味度和受欢迎度
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    # 蛋糕的美丽度、美味度和受欢迎度的最大值
    max_beauty = 0
    max_delicious = 0
    max_popular = 0
    # 蛋糕的美丽度、美味度和受欢迎度的最小值
    min_beauty = 0
    min_delicious = 0
    min_popular = 0
    # 蛋糕的美丽度、美味度和受欢迎度的绝对值的最大值
    max_abs_beauty = 0
    max_abs_delicious = 0
    max_abs_popular = 0
    # 蛋糕的美丽度、美味度和受欢迎度的绝对值的最小值
    min_abs_beauty = 0
    min_abs_delicious = 0
    min_abs_popular = 0
    # 蛋糕的美丽度、美味度和受欢迎度的绝对值的最大值的和
    max_abs_sum = 0
    # 蛋糕的美丽度、美味度和受欢迎度的绝对值的最小值的和
    min_abs_sum = 0
    # 蛋糕的美丽度、美味度和受欢迎度的最大值的和
    max_sum = 0
    # 蛋糕的美丽度、美味度和受欢迎度的最小值的和
    min_sum = 0
    # 蛋糕的美丽度、美味度和受欢迎

=======
Suggestion 10

def solve():
    n, m = map(int, input().split())
    cakes = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        cakes.append((x, y, z))
    ans = 0
    for i in range(1 << 3):
        cakes.sort(key=lambda x: sum(x[j] * (-1 if i >> j & 1 else 1) for j in range(3)))
        ans = max(ans, sum(abs(sum(cakes[i][j] for i in range(m))) for j in range(3)))
    print(ans)
