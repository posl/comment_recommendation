Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_value(n, m, cakes):
    max_value = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                value = abs(cakes[i][0] + cakes[j][0] + cakes[k][0]) + abs(cakes[i][1] + cakes[j][1] + cakes[k][1]) + abs(cakes[i][2] + cakes[j][2] + cakes[k][2])
                if value > max_value:
                    max_value = value
    return max_value

=======
Suggestion 2

def abs_sum(a,b,c):
    return abs(a) + abs(b) + abs(c)

N, M = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(2**3):
    tmp = []
    for j in range(N):
        cnt = 0
        for k in range(3):
            if (i >> k) & 1:
                cnt += xyz[j][k]
            else:
                cnt -= xyz[j][k]
        tmp.append(cnt)
    tmp.sort(reverse=True)
    ans = max(ans, sum(tmp[:M]))

print(ans)

=======
Suggestion 3

def main():
    # 读入数据
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))

    # 找出最大值
    ans = 0
    for i in range(2 ** 3):
        # 从二进制数的最低位开始，判断该位是否为1
        # 如果是1，就把对应的蛋糕的值加起来
        # 如果是0，就把对应的蛋糕的值减去
        # 由于二进制数的最低位是1，所以先把蛋糕的值加起来
        total = 0
        for j in range(N):
            value = 0
            for k in range(3):
                if ((i >> k) & 1) == 1:
                    value += cakes[j][k]
                else:
                    value -= cakes[j][k]
            total += abs(value)

        # 更新答案
        ans = max(ans, total)

    # 打印答案
    print(ans)

=======
Suggestion 4

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
    ans = -1
    for i in range(2**3):
        sign = [1]*3
        for j in range(3):
            if i&(1<<j):
                sign[j] = -1
        tmp = []
        for j in range(N):
            tmp.append(sign[0]*X[j]+sign[1]*Y[j]+sign[2]*Z[j])
        tmp.sort(reverse=True)
        ans = max(ans,sum(tmp[:M]))
    print(ans)

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    cakes = [list(map(int,input().split())) for _ in range(N)]
    #print(cakes)
    ans = 0
    for i in range(2**3):
        #print(i)
        cake = []
        for j in range(N):
            tmp = 0
            for k in range(3):
                if ((i >> k) & 1):
                    tmp += cakes[j][k]
                else:
                    tmp -= cakes[j][k]
            cake.append(tmp)
        cake.sort(reverse=True)
        #print(cake)
        ans = max(ans,sum(cake[:M]))
    print(ans)

=======
Suggestion 6

def get_max(N,M,beauty,delicious,favorite):
    # 1.先按照美丽度排序
    # 2.从美丽度最高的开始取，直到取满M个
    # 3.取的时候，按照美味度排序
    # 4.取的时候，按照受欢迎度排序
    # 5.取的时候，按照美丽度排序
    # 6.取的时候，计算总和
    # 7.计算出来的总和，取最大的那个
    # 8.如果取不满M个，就从美丽度第二高的开始取，直到取满M个
    # 9.如果取不满M个，就从美丽度第三高的开始取，直到取满M个
    # 10.如果取不满M个，就从美丽度第四高的开始取，直到取满M个
    # 11.如果取不满M个，就从美丽度第五高的开始取，直到取满M个
    # 12.如果取不满M个，就从美丽度第六高的开始取，直到取满M个
    # 13.如果取不满M个，就从美丽度第七高的开始取，直到取满M个
    # 14.如果取不满M个，就从美丽度第八高的开始取，直到取满M个
    # 15.如果取不满M个，就从美丽度第九高的开始取，直到取满M个
    # 16.如果取不满M个，就从美丽度第十高的开始取，直到取满M个
    # 17.如果取不满M个，就从美丽度第十一高的开始取，直到取满M个
    #

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int,input().split())))
    cakes.sort(key=lambda x: -(abs(x[0])+abs(x[1])+abs(x[2])))
    ans = 0
    for i in range(m):
        ans += (abs(cakes[i][0])+abs(cakes[i][1])+abs(cakes[i][2]))
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int,input().split())))
    cakes.sort(key=lambda x:sum(x),reverse=True)
    ans = 0
    for i in range(m):
        ans += abs(cakes[i][0]) + abs(cakes[i][1]) + abs(cakes[i][2])
    print(ans)

=======
Suggestion 9

def f(n,m,lists):
    abs_lists = []
    for i in range(n):
        abs_lists.append([abs(lists[i][0]),abs(lists[i][1]),abs(lists[i][2])])
    abs_lists.sort(key=lambda x:x[0]+x[1]+x[2],reverse=True)
    print(abs_lists)
    ans = 0
    for i in range(m):
        ans += abs_lists[i][0]+abs_lists[i][1]+abs_lists[i][2]
    return ans

=======
Suggestion 10

def findMaxBeauty(cakes, m):
    cakes.sort(key=lambda cake: abs(cake[0]) + abs(cake[1]) + abs(cake[2]), reverse=True)
    # print(cakes)
    # print(cakes[0][0], cakes[0][1], cakes[0][2])
    beauty = abs(cakes[0][0])
    delicious = abs(cakes[0][1])
    popularity = abs(cakes[0][2])
    for i in range(1, m):
        beauty += abs(cakes[i][0])
        delicious += abs(cakes[i][1])
        popularity += abs(cakes[i][2])
    return beauty + delicious + popularity
