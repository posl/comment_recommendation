Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入数据
    n = int(input())
    # 计算结果
    result = (n - 1) // 100 + 1
    # 输出结果
    print(result)

=======
Suggestion 2

def main():
    N = int(input())
    if N % 100 == 0:
        print(N // 100)
    else:
        print(N // 100 + 1)

=======
Suggestion 3

def getCentury(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

=======
Suggestion 4

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

year = int(input())
print(century(year))

=======
Suggestion 5

def main():
    N = int(input("请输入年份："))
    print(N//100 + 1)

=======
Suggestion 6

def century_from_year(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

=======
Suggestion 7

def problem200_a():
    #解法1
    n = int(input())
    if n % 100 == 0:
        print(n // 100)
    else:
        print(n // 100 + 1)
    #解法2
    #print((n + 99) // 100)

=======
Suggestion 8

def century_from_year(year):
    if year % 100 == 0:
        return int(year / 100)
    else:
        return int(year / 100) + 1

=======
Suggestion 9

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
