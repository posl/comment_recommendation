Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 计算
    result = 0
    for i in A:
        if i > 10:
            result += i - 10
    # 打印输出
    print(result)

main()

=======
Suggestion 2

def problem204_b():
    N = int(input())
    A = list(map(int, input().split()))

    count = 0
    for i in range(N):
        if A[i] > 10:
            count += A[i] - 10

    print(count)

problem204_b()

=======
Suggestion 3

def get_nuts(nuts):
    nuts = list(map(int, nuts.split()))
    nuts = [i-10 for i in nuts if i > 10]
    return sum(nuts)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    print(ans)

=======
Suggestion 5

def get_nuts(nuts):
    nuts = list(map(int, nuts.split()))
    nuts.sort(reverse=True)
    nuts = list(filter(lambda x: x >= 10, nuts))
    nuts = list(map(lambda x: x - 10, nuts))
    return sum(nuts)

=======
Suggestion 6

def getNutsFromTree(nuts):
    nuts.sort(reverse=True)
    nuts.pop(0)
    return sum(nuts)

=======
Suggestion 7

def main():
    num = int(input())
    nuts = list(map(int,input().split()))
    total = 0
    for i in nuts:
        if i >= 10:
            total += i - 10
    print(total)

=======
Suggestion 8

def harvest_nuts(nuts):
    nuts = [int(nut) for nut in nuts]
    nuts.sort(reverse=True)
    nuts = [nut if nut < 10 else nut - 10 for nut in nuts]
    return sum(nuts)

=======
Suggestion 9

def get_nuts(nuts):
    sum = 0
    for nut in nuts:
        if nut > 10:
            sum += nut - 10
    return sum
