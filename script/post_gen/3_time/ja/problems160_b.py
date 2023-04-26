Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    ans = 0
    ans += x // 500 * 1000
    x %= 500
    ans += x // 5 * 5
    print(ans)

=======
Suggestion 2

def calc_joy(x):
    joy = 0
    while x >= 500:
        x -= 500
        joy += 1000
    while x >= 5:
        x -= 5
        joy += 5
    return joy

=======
Suggestion 3

def main():
    x = int(input())
    result = 0
    if x >= 500:
        result += (x // 500) * 1000
        x = x % 500
    if x >= 5:
        result += (x // 5) * 5
        x = x % 5
    print(result)

=======
Suggestion 4

def calculate_happiness(x):
    happiness = 0
    happiness += (x // 500) * 1000
    x = x % 500
    happiness += (x // 5) * 5
    return happiness

=======
Suggestion 5

def calc_happy(x):
    happy = 0
    happy += int(x / 500) * 1000
    x = x - int(x / 500) * 500
    happy += int(x / 5) * 5
    return happy

x = int(input())
print(calc_happy(x))

=======
Suggestion 6

def exchange(x):
    return x // 500 * 1000 + (x % 500) // 5 * 5

x = int(input())
print(exchange(x))

=======
Suggestion 7

def main():
    x = int(input())
    print(x//500*1000+(x%500)//5*5)

=======
Suggestion 8

def main():
    x = int(input())
    print(x//500*1000+x%500//5*5)

=======
Suggestion 9

def main():
    X = int(input())
    print(X//500*1000+X%500//5*5)

=======
Suggestion 10

def main():
    X = int(input())

    # 500円硬貨の枚数
    n_500 = X // 500
    # 500円硬貨を使った時の嬉しさ
    a_500 = n_500 * 1000
    # 500円硬貨を使った時の残り
    X = X - n_500 * 500

    # 5円硬貨の枚数
    n_5 = X // 5
    # 5円硬貨を使った時の嬉しさ
    a_5 = n_5 * 5

    # 嬉しさの合計
    a = a_500 + a_5

    print(a)
