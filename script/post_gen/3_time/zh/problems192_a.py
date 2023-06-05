Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    print(100 - (x % 100))

=======
Suggestion 2

def main():
    x = int(input())
    print(100 - x % 100)

=======
Suggestion 3

def get_extra_coin_num(coin_num):
    return 100 - coin_num % 100

=======
Suggestion 4

def solve():
    x = int(input())
    print(100 - x % 100)

=======
Suggestion 5

def main():
    x = int(input("请输入x的值："))
    if 0 <= x <= 10**5:
        print(100-x%100)
    else:
        print("输入的值不符合规范！")

=======
Suggestion 6

def main():
    x = int(input())
    if 0 <= x <= 100000:
        print(100 - x % 100)
    else:
        print("输入错误")

=======
Suggestion 7

def get_extra_coins(coins):
    if coins % 100 == 0:
        return 100
    else:
        return 100 - (coins % 100)
