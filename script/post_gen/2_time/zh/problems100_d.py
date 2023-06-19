Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_value(N,M,x,y,z):
    max_value = 0
    for i in range(0,N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                value = abs(x[i])+abs(x[j])+abs(x[k])+abs(y[i])+abs(y[j])+abs(y[k])+abs(z[i])+abs(z[j])+abs(z[k])
                if value > max_value:
                    max_value = value
    return max_value

N,M = map(int,input().split())
x = []
y = []
z = []
for i in range(0,N):
    x_i,y_i,z_i = map(int,input().split())
    x.append(x_i)
    y.append(y_i)
    z.append(z_i)

print(get_max_value(N,M,x,y,z))

=======
Suggestion 2

def cal():
    N,M = map(int,input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int,input().split())))
    ans = 0
    for sign in range(8):
        cakes.sort(key=lambda x: (sign&1)*x[0]-(sign&2)*x[0]-(sign&4)*x[0],reverse=True)
        sum = [0,0,0]
        for i in range(M):
            for j in range(3):
                sum[j] += cakes[i][j]
        ans = max(ans,abs(sum[0])+abs(sum[1])+abs(sum[2]))
    print(ans)

=======
Suggestion 3

def get_max_value(n, m, cakes):
    #美丽度
    beauty = [x for x, y, z in cakes]
    #美味度
    flavor = [y for x, y, z in cakes]
    #受欢迎度
    popular = [z for x, y, z in cakes]
    #总美丽度的绝对值
    beauty_abs = [abs(x) for x in beauty]
    #总美味度的绝对值
    flavor_abs = [abs(y) for y in flavor]
    #总受欢迎度的绝对值
    popular_abs = [abs(z) for z in popular]
    #总美丽度的绝对值+总美味度的绝对值+总受欢迎度的绝对值
    max_value = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                value = sum(beauty_abs[i:j+1]) + sum(flavor_abs[i:j+1]) + sum(popular_abs[i:j+1])
                if value > max_value:
                    max_value = value
    return max_value

=======
Suggestion 4

def get_max_value(N, M, cakes):
    # 1. 选出最大的M个蛋糕
    cakes.sort(key=lambda x: abs(x[0]) + abs(x[1]) + abs(x[2]), reverse=True)
    # 2. 计算最大的M个蛋糕的总美丽度、美味度和受欢迎度
    total_beauty = sum([cake[0] for cake in cakes[:M]])
    total_delicious = sum([cake[1] for cake in cakes[:M]])
    total_popularity = sum([cake[2] for cake in cakes[:M]])
    # 3. 如果有负值，则把负号去掉
    if total_beauty < 0:
        total_beauty = -total_beauty
    if total_delicious < 0:
        total_delicious = -total_delicious
    if total_popularity < 0:
        total_popularity = -total_popularity
    # 4. 返回最大的M个蛋糕的总美丽度、美味度和受欢迎度
    return total_beauty + total_delicious + total_popularity

=======
Suggestion 5

def readinput():
    n,m=list(map(int,input().split()))
    cakes=[]
    for _ in range(n):
        x,y,z=list(map(int,input().split()))
        cakes.append([x,y,z])
    return n,m,cakes

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int, input().split())))
    cakes.sort(key=lambda x: x[0]+x[1]+x[2], reverse=True)
    ans = 0
    for i in range(m):
        ans += cakes[i][0]+cakes[i][1]+cakes[i][2]
    print(ans)

=======
Suggestion 7

def maxvalue(n, m, cake):
    # n: 蛋糕种类数
    # m: 要吃的蛋糕数
    # cake: 蛋糕的美丽、美味、受欢迎度
    # 返回最大值
    cake.sort(key=lambda x: abs(x[0]) + abs(x[1]) + abs(x[2]), reverse=True)
    # 先按照综合排序
    # 然后按照美丽度排序
    cake.sort(key=lambda x: abs(x[0]), reverse=True)
    # 然后按照美味度排序
    cake.sort(key=lambda x: abs(x[1]), reverse=True)
    # 然后按照受欢迎度排序
    cake.sort(key=lambda x: abs(x[2]), reverse=True)
    # 然后按照综合排序
    # 然后按照美丽度排序
    # 然后按照美味度排序
    # 然后按照受欢迎度排序
    # 以上都是降序排列
    # 第一种蛋糕的综合值最大
    # 在综合值相同的情况下，美丽度最大
    # 在美丽度相同的情况下，美味度最大
    # 在美味度相同的情况下，受欢迎度最大
    # 在受欢迎度相同的情况下，蛋糕的种类最大
    # 以上就是排序的规则
    # 排序完成之后，选择前m个蛋糕的综合值
    # 返回

    result = 0
    for i in range(m):
        result += abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2])
    return result

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    cakes = []
    for _ in range(N):
        cakes.append(list(map(int, input().split())))
    max_score = 0
    for i in range(2 ** N):
        # print(i)
        # print(bin(i))
        # print(bin(i)[2:])
        # print(bin(i)[2:].zfill(N))
        # print(list(bin(i)[2:].zfill(N)))
        # print(list(map(int, list(bin(i)[2:].zfill(N)))))
        choice = list(map(int, list(bin(i)[2:].zfill(N))))
        if choice.count(1) != M:
            continue
        score = 0
        for j in range(N):
            if choice[j] == 0:
                continue
            score += abs(cakes[j][0]) + abs(cakes[j][1]) + abs(cakes[j][2])
        max_score = max(max_score, score)
    print(max_score)

=======
Suggestion 9

def cal_abs_max(l):
    l = sorted(l, key=abs, reverse=True)
    return sum(l[:3])

=======
Suggestion 10

def my_abs(x):
    if x > 0:
        return x
    else:
        return -x
