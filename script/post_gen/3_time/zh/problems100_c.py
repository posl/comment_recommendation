Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] /= 2
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] //= 2
            count += 1
    print(count)
    return 0

=======
Suggestion 3

def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 操作次数
    ans = 0
    # 遍历每个数
    for i in range(n):
        # 操作次数
        cnt = 0
        # 如果能整除2
        while a[i] % 2 == 0:
            a[i] /= 2
            cnt += 1
        # 更新操作次数
        ans += cnt
    # 输出结果
    print(ans)

=======
Suggestion 4

def solve(N, A):
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                return cnt
        cnt += 1

=======
Suggestion 5

def f():
    N = int(input())
    A = [int(i) for i in input().split()]
    result = 0
    for a in A:
        while a % 2 == 0:
            a /= 2
            result += 1
    print(result)
f()

=======
Suggestion 6

def solve(n, a):
    count = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            count += 1
    return count

=======
Suggestion 7

def solve(n, a):
    #print(n)
    #print(a)
    count = 0
    for i in range(n):
        while a[i]%2 == 0:
            a[i] = a[i]/2
            count += 1
    return count

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for a in A:
        while a % 2 == 0:
            a //= 2
            count += 1
    print(count)

=======
Suggestion 9

def div(a):
    if a % 2 == 0:
        return int(a / 2)
    else:
        return int(a)

=======
Suggestion 10

def count2(x):
    count = 0
    while x % 2 == 0:
        count += 1
        x = x // 2
    return count

n = int(input())
a = list(map(int, input().split()))

count = 0
for i in a:
    count += count2(i)

print(count)
