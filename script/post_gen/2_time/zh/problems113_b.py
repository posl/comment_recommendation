Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入输入
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    # 计算温度
    temp = [t - x * 0.006 for x in h]
    # 找到最接近的温度
    temp = [abs(x - a) for x in temp]
    # 打印结果
    print(temp.index(min(temp)) + 1)
    return

=======
Suggestion 2

def problems113_b():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min_diff = 100000
    for i in range(n):
        temp = t - h[i] * 0.006
        if abs(a - temp) < min_diff:
            min_diff = abs(a - temp)
            ans = i + 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    min = 100000000
    index = 0
    for i in range(N):
        temperature = T - H[i] * 0.006
        if abs(A - temperature) < min:
            min = abs(A - temperature)
            index = i + 1

    print(index)

=======
Suggestion 4

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min = float('inf')
    for i in range(n):
        temp = t - h[i] * 0.006
        if abs(temp - a) < min:
            min = abs(temp - a)
            ans = i + 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = [t - i * 0.006 for i in h]
    # print(h)
    # print([abs(i - a) for i in h])
    print([abs(i - a) for i in h].index(min([abs(i - a) for i in h])) + 1)

=======
Suggestion 6

def problems113_b():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 100000000
    index = 0
    for i in range(n):
        if abs(t - h[i]*0.006 - a) < min:
            min = abs(t - h[i]*0.006 - a)
            index = i
    print(index + 1)

=======
Suggestion 7

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min_diff = 100000000
    for i in range(n):
        temp = t - h[i] * 0.006
        if abs(temp - a) < min_diff:
            min_diff = abs(temp - a)
            ans = i + 1
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min_d = 10**6
    min_i = 0
    for i in range(n):
        d = abs(a - (t - h[i] * 0.006))
        if d < min_d:
            min_d = d
            min_i = i + 1
    print(min_i)

=======
Suggestion 9

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 100000000
    index = 0
    for i in range(n):
        if abs(a - (t - h[i] * 0.006)) < min:
            min = abs(a - (t - h[i] * 0.006))
            index = i + 1
    print(index)

=======
Suggestion 10

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min = 100000000
    index = 0
    for i in range(N):
        if abs(T - H[i] * 0.006 - A) < min:
            min = abs(T - H[i] * 0.006 - A)
            index = i + 1
    print(index)
