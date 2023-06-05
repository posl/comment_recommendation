Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min_b = min(B)
    max_a = max(A)

    print(max(0, min_b - max_a + 1))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(1, 1001):
        for j in range(n):
            if a[j] <= i and i <= b[j]:
                ans += 1
                break
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    x = 0
    for i in range(N):
        x = max(x, A[i])
    y = 1000
    for i in range(N):
        y = min(y, B[i])
    print(max(0, y - x + 1))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    min_num = max(A)
    max_num = min(B)
    if min_num <= max_num:
        print(max_num - min_num + 1)
    else:
        print(0)

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    min_a = min(a)
    max_b = max(b)
    print(max(0, max_b - min_a + 1))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min = a[0]
    max = b[0]
    for i in range(n):
        if min < a[i]:
            min = a[i]
        if max > b[i]:
            max = b[i]
    if min > max:
        print(0)
    else:
        print(max - min + 1)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0
    for x in range(1, 1001):
        flag = True
        for i in range(n):
            if x < a[i] or x > b[i]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

=======
Suggestion 8

def get_input():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    return n, a, b

=======
Suggestion 9

def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 计算答案
    ans = 0
    for x in range(1, 1001):
        for i in range(n):
            if not (a[i] <= x <= b[i]):
                break
        else:
            ans += 1
    # 输出答案
    print(ans)
