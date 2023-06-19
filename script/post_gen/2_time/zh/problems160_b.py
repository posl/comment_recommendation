Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = int(input())
    count = 0
    while X >= 500:
        count += 1000
        X -= 500
    while X >= 5:
        count += 5
        X -= 5
    print(count)

=======
Suggestion 2

def main():
    # 读取输入
    x = int(input())

    # 通过交换他的钱，使他得到两个500日元的硬币和四个5日元的硬币，他获得了2020个幸福点，这是可以获得的最大幸福点。
    # 他身无分文--或者说没有日元。
    # 他是一个亿万富翁--以日元计算。

    # 计算结果
    print(1000 * (x // 500) + 5 * ((x % 500) // 5))

=======
Suggestion 3

def main():
    x = int(input())
    print(int(x/500)*1000 + int((x%500)/5)*5)

=======
Suggestion 4

def main():
    x = int(input())
    a = x // 500
    b = (x - a * 500) // 5
    print(a * 1000 + b * 5)

=======
Suggestion 5

def get_max_happiness_point(money):
    happiness = 0
    happiness += money // 500 * 1000
    happiness += (money % 500) // 5 * 5
    return happiness

=======
Suggestion 6

def main():
    x = int(input())
    a = x // 500
    b = (x % 500) // 5
    print(1000 * a + 5 * b)
    return

main()

=======
Suggestion 7

def main():
    x = int(input())
    print(1000 * (x // 500) + 5 * ((x % 500) // 5))

=======
Suggestion 8

def main():
    x = int(input())
    print(x//500*1000+(x%500)//5*5)

=======
Suggestion 9

def main():
    X = int(input())
    print(X//500*1000 + (X%500)//5*5)

=======
Suggestion 10

def main():
    x = int(input())
    a = x // 500
    b = (x % 500) // 5
    print(a * 1000 + b * 5)
