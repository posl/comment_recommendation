Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] == 0:
            print(0)
        else:
            print(-1)
        return
    if a[0] == 1:
        print(-1)
        return
    if a[-1] == 0:
        print(-1)
        return
    if n == 2:
        if a[0] == a[1]:
            print(0)
            return
        else:
            print(-1)
            return
    if a[0] == 0 and a[1] == 0:
        print(-1)
        return
    if a[0] == 0 and a[1] == 1 and a[2] == 1:
        print(-1)
        return
    if a[0] == 0 and a[1] == 1 and a[2] == 0:
        a[0] = 1
        a[1] = 0
        a[2] = 1
    if a[0] == 1 and a[1] == 0 and a[2] == 0:
        a[0] = 0
        a[1] = 1
        a[2] = 1
    if a[0] == 1 and a[1] == 0 and a[2] == 1:
        a[0] = 0
        a[1] = 1
        a[2] = 0
    if a[0] == 1 and a[1] == 1 and a[2] == 0:
        a[0] = 0
        a[1] = 0
        a[2] = 1
    if a[0] == 1 and a[1] == 1 and a[2] == 1:
        a[0] = 0
        a[1] = 0
        a[2] = 0
    for i in range(3, n):
        if a[i] == 0:
            continue
        if a[i - 1] == 0 and a[i - 2] == 0:
            print(-1)

=======
Suggestion 3

def print_good_choice_set(N, arr):
    # 1. find all the balls
    # 2. find all the boxes
    # 3. find all the boxes which are multiple of the ball
    # 4. if the total number of balls in the boxes are even, then it is a good choice set
    # 5. if the total number of balls in the boxes are odd, then it is a bad choice set
    # 6. if it is a bad choice set, then return -1
    # 7. if it is a good choice set, then return the ball number in the boxes
    # 8. if there is no ball in the boxes, then return 0

    # 1. find all the balls
    balls = []
    for i in range(N):
        if arr[i] == 1:
            balls.append(i+1)
    # 2. find all the boxes
    boxes = []
    for i in range(N):
        boxes.append(i+1)
    # 3. find all the boxes which are multiple of the ball
    multiple_boxes = []
    for ball in balls:
        for box in boxes:
            if box % ball == 0:
                multiple_boxes.append(box)
    # 4. if the total number of balls in the boxes are even, then it is a good choice set
    # 5. if the total number of balls in the boxes are odd, then it is a bad choice set
    # 6. if it is a bad choice set, then return -1
    # 7. if it is a good choice set, then return the ball number in the boxes
    # 8. if there is no ball in the boxes, then return 0
    if len(multiple_boxes) == 0:
        print(0)
    elif len(multiple_boxes) % 2 == 0:
        print(len(multiple_boxes))
        for box in multiple_boxes:
            print(box)
    else:
        print(-1)

=======
Suggestion 4

def main():
    print("hello world")

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    # N = 100
    # A = [0 for i in range(100)]

    # 先假设所有盒子都不放球
    # 如果盒子i上写的数字是1，则需要在i的倍数的盒子里放球
    # 如果盒子i上写的数字是0，则不需要在i的倍数的盒子里放球
    # 为了满足条件，需要在i的倍数的盒子里放球的个数，应该是i的倍数的盒子里球的个数的两倍
    # 为了满足条件，需要在i的倍数的盒子里放球的个数，应该是i的倍数的盒子里球的个数的两倍
    # 举例说明：
    # 盒子1上写1，盒子2上写0，盒子3上写0，盒子4上写0，盒子5上写0
    # 需要在盒子1、2、3、4、5里面放球
    # 盒子1里面放了1个球，盒子2里面放了0个球，盒子3里面放了0个球，盒子4里面放了0个球，盒子5里面放了0个球
    # 盒子1里面放了1个球，盒子2里面放了0个球，盒子3里面放了0个球，盒子4里面放了0个球，盒子5里面放了0个球
    # 盒子1里面放了1个球，盒子2里面放了0个球，盒子3里面放了0个球，盒子4里面放了0个球，盒子5里面放了0个球
    # 盒子1里面放了1个球，盒子2里面放了0个球，盒子3里面

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0] * n
    c = [0] * n
    for i in range(n):
        if a[i] == 1:
            b[i] = 1
            c[i] = 1
    for i in range(n):
        if b[i] == 1:
            for j in range(i+1,n,i+1):
                b[j] = 1 - b[j]
    for i in range(n-1,-1,-1):
        if c[i] == 1:
            for j in range(i-1,-1,-i):
                c[j] = 1 - c[j]
    d = []
    for i in range(n):
        if b[i] == c[i]:
            d.append(i+1)
    print(len(d))
    if len(d) > 0:
        print(" ".join(map(str,d)))

=======
Suggestion 7

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N, 0, -1):
        if sum(b[i-1::i]) % 2 != a[i-1]:
            b[i-1] = 1
    M = sum(b)
    print(M)
    if M != 0:
        print(' '.join(map(str, [i+1 for i in range(N) if b[i]])))

=======
Suggestion 8

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N, 0, -1):
        if a[i-1] == 1:
            ans.append(i)
            for j in range(1, int(i**0.5)+1):
                if i % j == 0:
                    a[j-1] = 1 - a[j-1]
                    if j != i // j:
                        a[i//j-1] = 1 - a[i//j-1]
    M = sum(a)
    if M == 0:
        print(0)
    else:
        print(M)
        print(*ans[::-1])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n-1, -1, -1):
        if sum(b[i::i+1]) % 2 != a[i]:
            b[i] = 1
    print(sum(b))
    print(*[i+1 for i in range(n) if b[i] == 1])
