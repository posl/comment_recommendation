Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print((b - a) * (b - a - 1) // 2 - a)

=======
Suggestion 2

def get_sum(n):
    return int((1 + n) * n / 2)

=======
Suggestion 3

def snow_covering(a, b):
    return b - a - 1

=======
Suggestion 4

def p099_b():
    a,b = map(int,input().split())
    print((b-a)*(b-a+1)//2-b)

p099_b()

=======
Suggestion 5

def snow(a,b):
    return b-a-1

=======
Suggestion 6

def snow(a, b):
    total = 0
    for i in range(1, a):
        total += i
    for i in range(b+1):
        total += i
    return total - a - b

=======
Suggestion 7

def snow(a, b):
    # 雪覆盖的深度
    x = 0
    # 求和
    sum = 0
    for i in range(1, 1000):
        sum += i
        if sum >= a:
            # 雪覆盖的深度
            x = i
            break
    return x

=======
Suggestion 8

def solve(a, b):
    return b - a - 1

print(solve(8, 13))
print(solve(54, 65))

=======
Suggestion 9

def get_hight(a, b):
    hight = 0
    for i in range(1, 1000):
        hight += i
        if hight == a:
            hight = i
            break
    return hight

=======
Suggestion 10

def main():
    a,b = map(int,input().split())
    print((b-a-1)*b//2 - a)
