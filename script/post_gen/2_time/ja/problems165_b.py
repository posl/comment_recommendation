Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    money = 100
    year = 0
    while money < x:
        money = int(money * 1.01)
        year += 1
    print(year)

=======
Suggestion 2

def main():
    x = int(input())
    money = 100
    year = 0
    while True:
        year += 1
        money = int(money * 1.01)
        if money >= x:
            break
    print(year)

=======
Suggestion 3

def main():
    x = int(input())
    y = 100
    count = 0
    while y < x:
        y = int(y * 1.01)
        count += 1
    print(count)

=======
Suggestion 4

def main():
    x = int(input())
    y = 100
    cnt = 0
    while y < x:
        y = int(y * 1.01)
        cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    x = int(input())
    y = 100
    i = 0
    while y < x:
        y = int(y * 1.01)
        i += 1
    print(i)

=======
Suggestion 6

def main():
    x = int(input())
    money = 100
    year = 0
    while money < x:
        money = money + (money // 100)
        year = year + 1
    print(year)

=======
Suggestion 7

def calcYear(x):
    y = 0
    z = 100
    while z < x:
        z += z // 100
        y += 1
    return y

x = int(input())
print(calcYear(x))

=======
Suggestion 8

def getYear(x):
    y = 0
    a = 100
    while True:
        a = int(a * 1.01)
        y += 1
        if a >= x:
            return y

x = int(input())
print(getYear(x))

=======
Suggestion 9

def calc_deposit_year(deposit):
    year = 0
    while deposit < X:
        deposit += deposit//100
        year += 1
    return year
