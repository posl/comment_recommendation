Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min_t = float('inf')
    for i in range(n):
        tmp = t - h[i] * 0.006
        if abs(tmp - a) < min_t:
            min_t = abs(tmp - a)
            ans = i + 1
    print(ans)

=======
Suggestion 2

def problems113_b():
    pass

=======
Suggestion 3

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min_diff = 10**6
    for i in range(n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)

=======
Suggestion 4

def get_input():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    return N, T, A, H

=======
Suggestion 5

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = list(map(lambda x: abs(a - (t - x * 0.006)), h))
    print(h.index(min(h)) + 1)

=======
Suggestion 6

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min = 100000
    index = 0
    for i in range(N):
        if abs(A - (T - H[i] * 0.006)) < min:
            min = abs(A - (T - H[i] * 0.006))
            index = i + 1
    print(index)

=======
Suggestion 7

def main():
    #输入
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    #计算
    #地点i的平均温度是T-H[i]*0.006摄氏度。
    #因此，宫殿应该建在地点i。
    #平均温度最接近A摄氏度的地方
    #打印应该建造宫殿的地方的索引。
    #保证该方案是唯一的。
    #输出
    #打印应该建造宫殿的地方的索引。
    #print(H)
    #print(T)
    #print(A)
    #print(N)
    #print(H[0])
    #print(T-H[0]*0.006)
    #print(abs(A-(T-H[0]*0.006)))
    #print(abs(A-(T-H[0]*0.006)) - abs(A-(T-H[1]*0.006)))
    #print(abs(A-(T-H[0]*0.006)) - abs(A-(T-H[2]*0.006)))
    #print(abs(A-(T-H[1]*0.006)) - abs(A-(T-H[2]*0.006)))
    #print(abs(A-(T-H[1]*0.006)) - abs(A-(T-H[0]*0.006)))
    #print(abs(A-(T-H[2]*0.006)) - abs(A-(T-H[0]*0.006)))
    #print(abs(A-(T-H[2]*0.006)) - abs(A-(T-H[1]*0.006)))
    #print(abs(A-(T-H[2]*0.006)) - abs(A-(T-H[2]*0.006)))
    #print(abs(A-(T-H[2]*0.006)) - abs(A-(T-H[1]*0.006)))
    #print(abs(A-(T-H[2]*0.006)) - abs(A-(T-H[0]*0.006)))
    #print(abs(A-(T-H[1]*0.006)) - abs(A-(T-H[0]*0.006)))
    #print(abs(A

=======
Suggestion 8

def f():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = [abs(a - (t - i * 0.006)) for i in h]
    print(h.index(min(h)) + 1)

=======
Suggestion 9

def get_input():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    return n, t, a, h
