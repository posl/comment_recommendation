Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    x,y,z = [],[],[]
    for i in range(n):
        x_i,y_i,z_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
        z.append(z_i)
    x.sort(reverse=True)
    y.sort(reverse=True)
    z.sort(reverse=True)
    ans = 0
    for i in range(2**3):
        sign = [1]*3
        for j in range(3):
            if (i>>j)&1:
                sign[j] = -1
        x_sum,y_sum,z_sum = 0,0,0
        for j in range(m):
            x_sum += x[j]*sign[0]
            y_sum += y[j]*sign[1]
            z_sum += z[j]*sign[2]
        ans = max(ans,abs(x_sum)+abs(y_sum)+abs(z_sum))
    print(ans)

=======
Suggestion 2

def main():
    #问题陈述
    #高桥成为了一名糕点师，为了庆祝AtCoder初级竞赛100强，他开了一家商店La Confiserie d'ABC。
    #该店出售N种蛋糕。
    #每种蛋糕有三个参数 "美丽"、"美味 "和 "受欢迎"。第i种蛋糕的美丽度为x_i，美味度为y_i，受欢迎度为z_i。
    #这些值可能是零或负值。
    #Ringo已经决定在这里吃M块蛋糕。他将按以下方式选择蛋糕的集合：
    #不要有两块或两块以上相同种类的蛋糕。
    #在上述条件下，选择一组蛋糕，使（总美丽度的绝对值）+（总美味度的绝对值）+（总受欢迎程度的绝对值）最大化。
    #找出Ringo选择的这组蛋糕的（总美丽度的绝对值）+（总美味度的绝对值）+（总受欢迎程度的绝对值）的最大可能值。
    #
    #约束条件
    #N是1到1 000（包括）之间的整数。
    #M是0到N之间的一个整数（包括）。
    #x_i, y_i, z_i (1 ≦ i ≦ N)是介于-10 000 000和10 000 000（包括）之间的整数。
    #
    #输入
    #输入来自标准输入，其格式如下：
    #N M
    #X_1 Y_1 Z_1
    #x_2 y_2 z_2
    #

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    X = []
    Y = []
    Z = []
    for i in range(N):
        x,y,z = map(int,input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)
    max = 0
    for i in range(2**3):
        x = 1
        y = 1
        z = 1
        for j in range(3):
            if i & 1<<j:
                x *= -1
            if i & 1<<(j+1):
                y *= -1
            if i & 1<<(j+2):
                z *= -1
        X.sort(reverse=True)
        Y.sort(reverse=True)
        Z.sort(reverse=True)
        s = 0
        for j in range(M):
            s += (X[j]*x + Y[j]*y + Z[j]*z)
        if max < s:
            max = s
    print(max)

=======
Suggestion 4

def max_sum(N,M,X,Y,Z):
    #N:蛋糕种类
    #M:吃蛋糕数量
    #X:蛋糕美丽度
    #Y:蛋糕美味度
    #Z:蛋糕受欢迎度
    #返回值：最大可能值
    #方法：贪心算法
    #思路：先从N个蛋糕中找出M个蛋糕，使得（总美丽度的绝对值）+（总美味度的绝对值）+（总受欢迎度的绝对值）最大化
    #      再从剩下的N-M个蛋糕中找出M个蛋糕，使得（总美丽度的绝对值）+（总美味度的绝对值）+（总受欢迎度的绝对值）最大化
    #      最后从剩下的N-2M个蛋糕中找出M个蛋糕，使得（总美丽度的绝对值）+（总美味度的绝对值）+（总受欢迎度的绝对值）最大化
    #      最后三次找出的蛋糕的集合即为最终结果
    #      因为N-M>=M>=1，所以最后一次找出的蛋糕集合不会为空
    #      所以最终结果集合中的蛋糕数量为3M
    #      由于每次找出的蛋糕集合不会重复，所以最终结果集合中的蛋糕不会重复
    #      最终结果集合中的蛋糕数量为3M，所以最终结果集合中的蛋

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int, input().split())))
    cakes.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    ans = 0
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if i + j + k <= m:
                    sum = 0
                    for l in range(i):
                        sum += cakes[l][0]
                    for l in range(j):
                        sum += cakes[l][1]
                    for l in range(k):
                        sum += cakes[l][2]
                    ans = max(ans, abs(sum))
    print(ans)

=======
Suggestion 6

def get_max_value(cakes, m):
    cakes.sort(key=lambda x: abs(x[0]) + abs(x[1]) + abs(x[2]), reverse=True)
    values = []
    for i in range(1, 2**len(cakes)):
        cakes_selected = []
        for j in range(len(cakes)):
            if (i >> j) % 2 == 1:
                cakes_selected.append(cakes[j])
        if len(cakes_selected) == m:
            values.append(sum([abs(cake[0]) + abs(cake[1]) + abs(cake[2]) for cake in cakes_selected]))
    return max(values)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**3):
        sign = [-1, -1, -1]
        if (i & 1):
            sign[0] = 1
        if (i & 2):
            sign[1] = 1
        if (i & 4):
            sign[2] = 1
        cakes.sort(key=lambda x: sum([sign[j] * x[j] for j in range(3)]), reverse=True)
        ans = max(ans, sum([abs(sum([sign[j] * cakes[k][j] for j in range(3)])) for k in range(M)]))
    print(ans)

=======
Suggestion 8

def problems100_d():
    n,m = map(int,input().split())
    x = []
    y = []
    z = []
    for i in range(n):
        x_i,y_i,z_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
        z.append(z_i)
    print(x)
    print(y)
    print(z)

    sum_list = []
    for i in range(2**n):
        sum_x = 0
        sum_y = 0
        sum_z = 0
        for j in range(n):
            if ((i>>j)&1):
                sum_x += x[j]
                sum_y += y[j]
                sum_z += z[j]
        sum_list.append([sum_x,sum_y,sum_z])
    print(sum_list)

    max_sum = 0
    for i in range(len(sum_list)):
        for j in range(len(sum_list)):
            for k in range(len(sum_list)):
                if (sum_list[i][0]+sum_list[j][1]+sum_list[k][2])>max_sum:
                    max_sum = sum_list[i][0]+sum_list[j][1]+sum_list[k][2]
    print(max_sum)

problems100_d()

=======
Suggestion 9

def get_max_abs_sum(a):
    n = len(a)
    s = 0
    for i in range(n):
        s += abs(a[i])
    return s

=======
Suggestion 10

def problem100_d():
    return
