Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_num_list(h1,h2,h3,w1,w2,w3):
    num_list = []
    for i in range(1,31):
        for j in range(1,31):
            for k in range(1,31):
                for l in range(1,31):
                    for m in range(1,31):
                        for n in range(1,31):
                            if i+j+k == h1 and l+m+n == h2 and i+l == w1 and j+m == w2 and k+n == w3 and i+l+m == h3:
                                num_list.append([i,j,k,l,m,n])
    return num_list

=======
Suggestion 2

def solve(h1,h2,h3,w1,w2,w3):
    if sum([h1,h2,h3]) != sum([w1,w2,w3]):
        return 0
    else:
        return 1

=======
Suggestion 3

def solve(h1,h2,h3,w1,w2,w3):
    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                for l in range(1,10):
                    for m in range(1,10):
                        for n in range(1,10):
                            if i + j + k == h1 and l + m + n == h2 and i + l == w1 and j + m == w2 and k + n == w3 and i + j + k == h1 and l + m + n == h2 and i + l == w1 and j + m == w2 and k + n == w3:
                                ans += 1
    return ans

=======
Suggestion 4

def f(h,w):
    if h==[]:
        return 1
    else:
        res = 0
        for i in range(1,h[0]+1):
            res += f(h[1:],w[1:])
        return res

h = list(map(int,input().split()))
w = list(map(int,input().split()))
print(f(h,w))

=======
Suggestion 5

def f(h, w):
    # 3行3列，每行每列的和分别为h1,h2,h3,w1,w2,w3
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 1+2+3=h1
    # 4+5+6=h2
    # 7+8+9=h3
    # 1+4+7=w1
    # 2+5+8=w2
    # 3+6+9=w3
    # h1+h2+h3=15
    # w1+w2+w3=24
    # 1+5+9=h1+h2+h3
    # 3+5+7=h1+h2+h3
    # 1+2+3=h1
    # 4+5+6=h2
    # 7+8+9=h3
    # 1+4+7=w1
    # 2+5+8=w2
    # 3+6+9=w3
    # h1+h2+h3=15
    # w1+w2+w3=24
    # 1+5+9=h1+h2+h3
    # 3+5+7=h1+h2+h3
    # 1+2+3=h1
    # 4+5+6=h2
    # 7+8+9=h3
    # 1+4+7=w1
    # 2+5+8=w2
    # 3+6+9=w3
    # h1+h2+h3=15
    # w1+w2+w3=24
    # 1+5+9=h1+h2+h3
    # 3+5+7=h1+h2+h3
    # 1+2+3=h1
    # 4+5+6=h2
    # 7+8+9=h3
    # 1+4+7=w1
    # 2+5+8=w2
    # 3+6+9=w3
    # h1+h2+h3=15
    # w1+w2+w

=======
Suggestion 6

def dfs(i, j, h, w):
    if i == 2 and j == 2:
        if h[0] == 0 and h[1] == 0 and h[2] == 0 and w[0] == 0 and w[1] == 0 and w[2] == 0:
            return 1
        else:
            return 0
    if j == 2:
        j = 0
        i += 1
    if h[i] < 0 or w[j] < 0:
        return 0
    res = 0
    for k in range(10):
        h[i] -= k
        w[j] -= k
        res += dfs(i, j + 1, h, w)
        h[i] += k
        w[j] += k
    return res

=======
Suggestion 7

def main():
    h = [int(i) for i in input().split()]
    w = [int(i) for i in input().split()]
    print(solve(h, w))

=======
Suggestion 8

def main():
    # 输入
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    # 用于计算的数组
    h = [h1, h2, h3]
    w = [w1, w2, w3]

    # 满足条件的数字写法的数量
    count = 0

    # 满足条件的数字写法的数量
    for i in range(1, h[0] + 1):
        for j in range(1, w[0] + 1):
            for k in range(1, h[1] + 1):
                for l in range(1, w[1] + 1):
                    for m in range(1, h[2] + 1):
                        for n in range(1, w[2] + 1):
                            if i + j == h[0] and i + k + m == h[1] and j + l + n == h[2] and k + l == w[0] and m + n == w[1] and i + l + m == w[2]:
                                count += 1

    # 输出
    print(count)

=======
Suggestion 9

def f(h1,h2,h3,w1,w2,w3):
    return 0
