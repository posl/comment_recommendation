Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def calc_fee(age, fee):
    if age >= 13:
        return fee
    elif age >= 6 and age <= 12:
        return fee / 2
    else:
        return 0

=======
Suggestion 2

def problem127_a():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(int(b/2))
    else:
        print(0)

problem127_a()

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif 6 <= A <= 12:
        print(int(B/2))
    else:
        print(0)

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(b//2)
    else:
        print(0)

=======
Suggestion 5

def main():
    age, fee = map(int, input().split())
    if age >= 13:
        print(fee)
    elif age >= 6:
        print(fee // 2)
    else:
        print(0)

=======
Suggestion 6

def main():
    # 读取输入
    A, B = map(int, input().split())

    # 计算结果
    if A >= 13:
        result = B
    elif A >= 6:
        result = B // 2
    else:
        result = 0

    # 输出结果
    print(result)

=======
Suggestion 7

def calc_fee(age, fee):
    if age <= 5:
        return 0
    elif age <= 12:
        return fee // 2
    else:
        return fee

=======
Suggestion 8

def main():
    age, price = map(int, input().split())
    if age >= 13:
        print(price)
    elif age >= 6:
        print(price//2)
    else:
        print(0)
