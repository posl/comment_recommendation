Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while sum(h) > 0:
        l, r = -1, -1
        for i in range(n):
            if h[i] > 0 and l == -1:
                l = i
            if h[i] == 0 and l != -1:
                r = i - 1
                break
        if r == -1:
            r = n - 1
        for i in range(l, r + 1):
            h[i] -= 1
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    h.append(0)
    ans = 0

    for i in range(1, N+1):
        if h[i-1] < h[i] and h[i] > h[i+1]:
            ans += 1
        elif h[i-1] > h[i] and h[i] < h[i+1]:
            ans += 1

    print(ans)

=======
Suggestion 3

def water_flower(h):
    #print(h)
    min_h = min(h)
    max_h = max(h)
    min_index = h.index(min_h)
    max_index = h.index(max_h)
    if min_h == max_h:
        return 0
    else:
        if min_index < max_index:
            for i in range(min_index,max_index):
                h[i] += 1
        else:
            for i in range(max_index,min_index):
                h[i] += 1
        return 1 + water_flower(h)

=======
Suggestion 4

def get_min_watering_times(N, h):
    left = 0
    right = 0
    count = 0
    for i in range(N):
        if h[i] == 0:
            continue
        if left == 0:
            left = i + 1
            right = i + 1
            count += h[i]
        else:
            if i + 1 == right:
                count += h[i]
            else:
                count += h[i] * (i + 1 - left)
            right = i + 1
    return count

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += h[i]
        else:
            if h[i-1] < h[i]:
                ans += h[i] - h[i-1]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    count = 0
    while sum(h) > 0:
        count += 1
        i = 0
        while i < n:
            if h[i] > 0:
                j = i
                while j < n and h[j] > 0:
                    h[j] -= 1
                    j += 1
                break
            i += 1
    print(count)

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    #读入数据
    n = int(input())
    h = list(map(int, input().split()))
    #定义一个变量来记录浇水的次数
    count = 0
    #对于每个花，都要浇水，所以从0到n遍历
    for i in range(n):
        #如果当前花的高度小于它的编号，则需要浇水
        if h[i] < i + 1:
            #浇水的量就是编号减去当前花的高度
            count += i + 1 - h[i]
            #浇水后，当前花的高度就是编号
            h[i] = i + 1
    #输出浇水的次数
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            count += h[i]
        else:
            if h[i] > h[i - 1]:
                count += h[i] - h[i - 1]
    print(count)

=======
Suggestion 10

def water_the_flowers(N, h):
    #不要忘记最后一个花朵
    h.append(0)
    #初始化
    l = 0
    r = 0
    #花朵高度
    hight = 0
    #浇水次数
    count = 0
    #当r小于N时，循环
    while r < N:
        #如果花朵高度等于0，l和r都加1
        if hight == 0:
            l += 1
            r += 1
            #花朵高度加1
            hight += 1
        #如果花朵高度不等于0，r加1
        else:
            r += 1
            #如果花朵高度小于r-l+1，花朵高度加1
            if hight < r - l + 1:
                hight += 1
            #如果花朵高度大于r-l+1，花朵高度减1
            elif hight > r - l + 1:
                hight -= 1
            #如果花朵高度等于r-l+1，花朵高度不变
            else:
                pass
        #浇水次数加1
        count += 1
    return count
