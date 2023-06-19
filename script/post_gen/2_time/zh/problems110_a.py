Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int, input().split())
    print(max(a+b+c, a+b*c, a*b+c, a*b*c))

=======
Suggestion 2

def main():
    A,B,C = map(int,input().split())
    print(max(A+B+C,10*A+B+C,A+10*B+C,A+B+10*C))

=======
Suggestion 3

def solve():
    a, b, c = map(int, input().split())
    print(a + b + c + max(a, b, c) * 9)

solve()

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(10 * A + B + C)

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    print(a+b+c+max(a,b,c)*9)

=======
Suggestion 6

def main():
    # 读取A,B,C
    a, b, c = map(int, input().split())

    # 通过穷举法找出最大值
    max = 0
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                # 通过这种方法将三个数字排列成一个三位数
                num = i * 100 + j * 10 + k

                # 如果num小于等于C，则直接跳过
                if num <= c:
                    continue

                # 如果num小于等于B，则直接跳过
                if num <= b:
                    continue

                # 如果num小于等于A，则直接跳过
                if num <= a:
                    continue

                # 如果num大于max，则将num赋值给max
                if num > max:
                    max = num

    # 打印结果
    print(max)
