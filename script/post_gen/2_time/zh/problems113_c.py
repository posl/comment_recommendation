Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    print(min(range(n), key=lambda i: abs(a - (t - h[i] * 0.006))) + 1)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def judge_temperature(n,t,a,h):
    """
    n:地点个数
    t:海拔高度
    a:温度
    h:地点海拔高度列表
    """
    #计算平均温度
    temperature = t - a * 0.006
    #计算每个地点的平均温度
    temperature_list = []
    for i in range(n):
        temperature_list.append(temperature - h[i] * 0.006)
    #找到最接近的温度
    min_temperature = temperature_list[0]
    min_index = 0
    for i in range(n):
        if abs(temperature_list[i] - temperature) < abs(min_temperature - temperature):
            min_index = i
            min_temperature = temperature_list[i]
    return min_index + 1

=======
Suggestion 4

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min_diff = 100000000000
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            ans = i + 1
            min_diff = diff
    print(ans)

=======
Suggestion 5

def solve():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 100000
    res = 0
    for i in range(len(h)):
        if abs(t - h[i] * 0.006 - a) < min:
            min = abs(t - h[i] * 0.006 - a)
            res = i + 1
    print(res)

=======
Suggestion 6

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min = 100000
    for i in range(n):
        if abs(min - a) > abs(t - h[i] * 0.006 - a):
            min = t - h[i] * 0.006
            ans = i + 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    T,A = map(int,input().split())
    H = list(map(int,input().split()))
    h = []
    for i in range(N):
        h.append(abs(A - (T - H[i]*0.006)))
    print(h.index(min(h)) + 1)

=======
Suggestion 8

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    temp = [t - x * 0.006 for x in h]
    print(temp.index(min(temp))+1)

=======
Suggestion 9

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
