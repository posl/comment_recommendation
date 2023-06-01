Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
print(2 * N // gcd(2, N))

=======
Suggestion 2

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n=int(input())
print(2*n//gcd(2,n))

=======
Suggestion 3

def lcm(x, y):
    return (x * y) // gcd(x, y)

=======
Suggestion 4

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


N = int(input())
print(N * 2 // gcd(N, 2))

=======
Suggestion 5

def main():
    N = int(input())
    print(N * 2)

=======
Suggestion 6

def main():
    # 读取输入
    n = int(input())
    # 初始化结果
    result = 1
    # 循环
    while True:
        # 判断
        if result % n == 0 and result % 2 == 0:
            # 打印结果
            print(result)
            # 结束循环
            break
        # 结果+1
        result += 1

=======
Suggestion 7

def main():
    N = int(input())
    print(2*N)

=======
Suggestion 8

def main():
    n = int(input())
    print(2*n)
