Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    t,a = map(int,input().split())
    h = list(map(int,input().split()))
    print(min(range(n),key=lambda i:abs(a-(t-h[i]*0.006)))+1)

=======
Suggestion 2

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 100000000
    index = 0
    for i in range(n):
        temp = t - h[i] * 0.006
        if abs(a - temp) < min:
            min = abs(a - temp)
            index = i
    print(index + 1)

=======
Suggestion 3

def get_index(temperature,altitude):
    min = 100000000
    index = 0
    for i in range(len(altitude)):
        if abs(temperature - (altitude[i] * 0.006)) < min:
            min = abs(temperature - (altitude[i] * 0.006))
            index = i
    return index + 1

=======
Suggestion 4

def problems113_b():
    return

=======
Suggestion 5

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    res = abs(a - (t - h[0] * 0.006))
    index = 1
    for i in range(1, n):
        tmp = abs(a - (t - h[i] * 0.006))
        if tmp < res:
            res = tmp
            index = i + 1
    print(index)

=======
Suggestion 6

def main():
    n = int(input())
    t,a = map(int,input().split())
    h = list(map(int,input().split()))
    h = [t-x*0.006 for x in h]
    print(h.index(min(h))+1)

=======
Suggestion 7

def main():
    # 输入
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    # 处理
    min_diff = 1000000
    min_index = 0
    for i in range(n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            min_index = i + 1

    # 输出
    print(min_index)

=======
Suggestion 8

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(abs(t - h[i] * 0.006 - a))
    print(b.index(min(b)) + 1)

=======
Suggestion 9

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min_diff = 1000000
    min_index = 0
    for i in range(N):
        temp = T - H[i] * 0.006
        if abs(A - temp) < min_diff:
            min_diff = abs(A - temp)
            min_index = i + 1
    print(min_index)

=======
Suggestion 10

def func():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    #print(H)
    min = 100000
    ans = 0
    for i in range(N):
        tmp = T - H[i] * 0.006
        if abs(A - tmp) < min:
            min = abs(A - tmp)
            ans = i + 1
    print(ans)
