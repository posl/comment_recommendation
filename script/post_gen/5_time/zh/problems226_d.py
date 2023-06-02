Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def get_min_spell_num(town_list):
    min_spell_num = 0
    return min_spell_num

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            a = x[i]-x[j]
            b = y[i]-y[j]
            c = 0
            d = 0
            for k in range(n):
                for l in range(k+1, n):
                    if x[k]-x[l] == a and y[k]-y[l] == b:
                        c += 1
                    if x[k]-x[l] == -a and y[k]-y[l] == -b:
                        d += 1
            res = max(res, n-c, n-d)
    print(res)
    return

=======
Suggestion 4

def get_distance(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def getMinNumOfSpell(N, x, y):
    spells = []
    for i in range(N):
        for j in range(N):
            if i != j:
                spells.append((x[j] - x[i], y[j] - y[i]))
    spells = list(set(spells))
    return len(spells)

=======
Suggestion 7

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            cnt = 0
            for k in range(n):
                for l in range(k+1, n):
                    if x[k] - x[l] == dx and y[k] - y[l] == dy:
                        cnt += 1
            ans = max(ans, n - cnt)
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    x.sort()
    y.sort()
    if n%2 == 1:
        x_med = x[n//2]
        y_med = y[n//2]
    else:
        x_med = (x[n//2-1]+x[n//2])//2
        y_med = (y[n//2-1]+y[n//2])//2
    ans = 0
    for i in range(n):
        ans += abs(x[i]-x_med) + abs(y[i]-y_med)
    print(ans)

=======
Suggestion 9

def getMinNumOfMagic(N, towns):
    # 1. 遍历所有城镇，计算城镇 i 到城镇 j 的距离，保存到数组中
    # 2. 遍历数组，计算数组中的元素的最大公约数
    # 3. 计算数组中的元素的最大公约数的最大公约数
    # 4. 返回最大公约数的最大公约数
    distance = []
    for i in range(0, N):
        for j in range(i+1, N):
            distance.append(abs(towns[i][0]-towns[j][0])+abs(towns[i][1]-towns[j][1]))
    # print(distance)
    # 2. 遍历数组，计算数组中的元素的最大公约数
    def getGCD(a, b):
        if b == 0:
            return a
        else:
            return getGCD(b, a%b)
    gcd = distance[0]
    for i in range(1, len(distance)):
        gcd = getGCD(gcd, distance[i])
    return gcd

=======
Suggestion 10

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
    xdiff = []
    ydiff = []
    for i in range(n-1):
        xdiff.append(x[i+1]-x[i])
        ydiff.append(y[i+1]-y[i])
    xdiff.sort()
    ydiff.sort()
    print(max(xdiff[-1],ydiff[-1]))
