Synthesizing 9/10 solutions

=======
Suggestion 1

def f(h, w):
    if h == 0 and w == 0:
        return 1
    elif h <= 0 or w <= 0:
        return 0
    elif dp[h][w] != -1:
        return dp[h][w]
    else:
        dp[h][w] = f(h-1, w) + f(h-1, w-1) + f(h-1, w-2) + f(h-2, w) + f(h-2, w-1) + f(h-3, w)
        return dp[h][w]

h1, h2, h3, w1, w2, w3 = map(int, input().split())
dp = [[-1 for _ in range(31)] for _ in range(31)]
print(f(h1, w1) * f(h2, w2) * f(h3, w3))

=======
Suggestion 2

def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    print(h1,h2,h3,w1,w2,w3)
    #h1,h2,h3,w1,w2,w3 = 3,4,6,3,3,7
    #h1,h2,h3,w1,w2,w3 = 3,4,5,6,7,8
    #h1,h2,h3,w1,w2,w3 = 5,13,10,6,13,9
    #h1,h2,h3,w1,w2,w3 = 20,25,30,22,29,24
    #h1,h2,h3,w1,w2,w3 = 3,4,5,6,7,8
    #h1,h2,h3,w1,w2,w3 = 3,4,6,3,3,7
    #h1,h2,h3,w1,w2,w3 = 3,4,5,6,7,8
    #h1,h2,h3,w1,w2,w3 = 5,13,10,6,13,9
    #h1,h2,h3,w1,w2,w3 = 20,25,30,22,29,24
    #h1,h2,h3,w1,w2,w3 = 3,4,5,6,7,8
    #h1,h2,h3,w1,w2,w3 = 3,4,6,3,3,7
    #h1,h2,h3,w1,w2,w3 = 3,4,5,6,7,8
    #h1,h2,h3,w1,w2,w3 = 5,13,10,6,13,9
    #h1,h2,h3,w1,w2,w3 = 20,25,30,22,29,24
    #h1,h2,h3,w1,w2,w3 = 3,4,5,6,7,8
    #h1,h2,h3,w1,w2,w3 = 3,4,6,3,3,7
    #h1,h2,h3,w1,w2,w3 =

=======
Suggestion 3

def main():
    h = [int(x) for x in input().split()]
    w = [int(x) for x in input().split()]
    print(h, w)
    # print('h1', h[0])
    # print('h2', h[1])
    # print('h3', h[2])
    # print('w1', w[0])
    # print('w2', w[1])
    # print('w3', w[2])
    # print('-----------')
    # print('h1+h2+h3', h[0]+h[1]+h[2])
    # print('w1+w2+w3', w[0]+w[1]+w[2])
    # print('-----------')

    # print('h1+h2', h[0]+h[1])
    # print('h2+h3', h[1]+h[2])
    # print('-----------')
    # print('w1+w2', w[0]+w[1])
    # print('w2+w3', w[1]+w[2])
    # print('-----------')

    # print('h1+h2+h3', h[0]+h[1]+h[2])
    # print('w1+w2+w3', w[0]+w[1]+w[2])
    # print('-----------')
    # print('h1+h2', h[0]+h[1])
    # print('h2+h3', h[1]+h[2])
    # print('-----------')
    # print('w1+w2', w[0]+w[1])
    # print('w2+w3', w[1]+w[2])
    # print('-----------')

    # print('h1+h2+h3', h[0]+h[1]+h[2])
    # print('w1+w2+w3', w[0]+w[1]+w[2])
    # print('-----------')
    # print('h1+h2', h[0]+h[1])
    # print('h2+h3', h[1]+h[2])
    # print('h1+h3', h[0]+h[2])
    # print('-----------')
    # print('w1+w2', w[0]+w[1])
    #

=======
Suggestion 4

def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    print(h1,h2,h3,w1,w2,w3)
    #print(h1+h2+h3,w1+w2+w3)
    if h1+h2+h3 != w1+w2+w3:
        print(0)
        return
    #print('h1+h2+h3 == w1+w2+w3')
    #print(h1,h2,h3,w1,w2,w3)
    if h1+w1 != h2+w2:
        print(0)
        return
    if h1+w1 != h3+w3:
        print(0)
        return
    #print('h1+w1 == h2+w2 == h3+w3')
    #print(h1,h2,h3,w1,w2,w3)
    if h1 == w1:
        print(1)
        return
    if h1 == w2:
        print(1)
        return
    if h1 == w3:
        print(1)
        return
    if h2 == w1:
        print(1)
        return
    if h2 == w2:
        print(1)
        return
    if h2 == w3:
        print(1)
        return
    if h3 == w1:
        print(1)
        return
    if h3 == w2:
        print(1)
        return
    if h3 == w3:
        print(1)
        return
    print(0)
    return

=======
Suggestion 5

def main():
    h = list(map(int, input().strip().split()))
    w = list(map(int, input().strip().split()))

    # 3*3的矩阵，所以一共9个位置
    # 9个位置中，每个位置都有9种填法，但是有条件，所以减少一些
    # 1.每行的和都是固定的，那么就可以确定第一行的任意一个位置的数
    # 2.第一列的和也是固定的，那么就可以确定第一列的任意一个位置的数
    # 3.第二行的和也是固定的，那么就可以确定第二行的任意一个位置的数
    # 4.第二列的和也是固定的，那么就可以确定第二列的任意一个位置的数
    # 5.第三行的和也是固定的，那么就可以确定第三行的任意一个位置的数
    # 6.第三列的和也是固定的，那么就可以确定第三列的任意一个位置的数
    # 7.对角线的和也是固定的，那么就可以确定对角线的任意一个位置的数
    # 8.对角线的和也是固定的，那么就可以确定对角线的任意一个位置的数

    # 1.确定第一行的任意一个位置的数
    # 2.确定第一列的任意一个位置的数
    # 3.确定第二行的任意一个位置的数
    # 4.确定第二列的任意一个位置的数
    # 5.确定第三行的任意一个位置的数
    # 6.确定第三列的任意一个位置的数
    # 7.确定对角线的任意一个位置的数
    # 8.确定对角线的任意一个位置的数
    # 9.确定对角线的任意一个

=======
Suggestion 6

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print(h1, h2, h3, w1, w2, w3)
    print(h1, h2, h3, w1, w2, w3)
    print(h1, h2, h3, w1, w2, w3)
    print(h1, h2, h3, w1, w2, w3)
    print(h1, h2, h3, w1, w2, w3)
    print(h1, h2, h3, w1, w2, w3)
    print(h1, h2, h3, w1, w2, w3)
    print(h1, h2, h3, w1, w2, w3)
    print(h1, h2, h3, w1, w2, w3)
    print(h1, h2, h3, w1, w2, w3)

=======
Suggestion 7

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print(solve(h1, h2, h3, w1, w2, w3))

=======
Suggestion 8

def f(h1,h2,h3,w1,w2,w3):
    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                for l in range(1,10):
                    for m in range(1,10):
                        for n in range(1,10):
                            if i+j+k==h1 and l+m+n==h2 and i+l==w1 and j+m==w2 and k+n==w3:
                                ans += 1
    return ans

h1,h2,h3,w1,w2,w3 = map(int,input().split())
print(f(h1,h2,h3,w1,w2,w3))

=======
Suggestion 9

def check(h1, h2, h3, w1, w2, w3):
    if h1+h2+h3 != w1+w2+w3:
        return False
    if h1+h2+h3 != w1+w2+w3:
        return False
    if h1+h2+h3 != w1+w2+w3:
        return False
    if h1+h2+h3 != w1+w2+w3:
        return False
    if h1+h2+h3 != w1+w2+w3:
        return False
    if h1+h2+h3 != w1+w2+w3:
        return False
    if h1+h2+h3 != w1+w2+w3:
        return False
    if h1+h2+h3 != w1+w2+w3:
        return False
    if h1+h2+h3 != w1+w2+w3:
        return False
    return True
