Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while (a[i] % 2 == 0):
            a[i] //= 2
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    # 读取输入
    N = int(input())
    a = list(map(int, input().split()))
    # 操作次数
    count = 0
    # 重复操作
    while True:
        # 检查是否可以继续操作
        for i in range(N):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                # 不能继续操作
                print(count)
                return
        # 操作次数加1
        count += 1

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if all([i % 2 == 0 for i in a]):
            a = [i // 2 for i in a]
            count += 1
        else:
            break
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        while a[i]%2 == 0:
            a[i] //= 2
            ans += 1

    print(ans)

=======
Suggestion 5

def judge(n):
    if n % 2 == 0:
        return True
    else:
        return False

=======
Suggestion 6

def count_divide_2(num):
    count = 0
    while num % 2 == 0:
        num = num // 2
        count += 1
    return count

n = int(input())
a = list(map(int, input().split()))

count = 0
for num in a:
    count += count_divide_2(num)

print(count)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] /= 2
            ans += 1

    print(ans)

=======
Suggestion 9

def divide2(n):
    return n/2
