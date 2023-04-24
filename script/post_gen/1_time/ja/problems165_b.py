Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    y = 100
    count = 0
    while y < x:
        y = int(y * 1.01)
        count += 1
    print(count)

=======
Suggestion 2

def main():
    x = int(input())
    money = 100
    cnt = 0
    while money < x:
        money = int(money * 1.01)
        cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    x = int(input())
    money = 100
    year = 0
    while money < x:
        money += money//100
        year += 1
    print(year)

=======
Suggestion 4

def main():
    x = int(input())
    ans = 0
    y = 100
    while y < x:
        y = int(y * 1.01)
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    # input
    X = int(input())
    # compute
    money = 100
    year = 0
    while money < X:
        money += money // 100
        year += 1
    # output
    print(year)

=======
Suggestion 6

def main():
    x = int(input())
    y = 100
    count = 0
    while y < x:
        y = y + int(y * 0.01)
        count += 1
    print(count)

=======
Suggestion 7

def calc_years(x):
    years = 0
    money = 100
    while money < x:
        money = int(money * 1.01)
        years += 1
    return years

x = int(input())
print(calc_years(x))

=======
Suggestion 8

def main():
    X = int(input())
    money = 100
    i = 1
    while True:
        money = money + int(money * 0.01)
        if money >= X:
            break
        i += 1
    print(i)

=======
Suggestion 9

def calc(x):
    y = 100
    i = 0
    while y < x:
        y = int(y*1.01)
        i += 1
    print(i)

x = int(input())
calc(x)

=======
Suggestion 10

def calc_years(x):
    y = 100
    years = 0
    while y < x:
        y = (y * 101) // 100
        years += 1
    return years

x = int(input())
print(calc_years(x))
