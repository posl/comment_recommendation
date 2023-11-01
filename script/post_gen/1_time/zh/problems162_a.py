Synthesizing 10/10 solutions

=======
Suggestion 1

def is_7_in_number(n):
    if n % 10 == 7:
        return True
    elif n < 10:
        return False
    else:
        return is_7_in_number(n // 10)

=======
Suggestion 2

def checkSeven(n):
    if n % 10 == 7:
        return True
    elif n < 10:
        return False
    else:
        return checkSeven(n // 10)

=======
Suggestion 3

def main():
    n = int(input())
    if n % 10 == 7 or n // 10 % 10 == 7 or n // 100 == 7:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    if N % 10 == 7:
        print("Yes")
    elif N // 10 % 10 == 7:
        print("Yes")
    elif N // 100 %

=======
Suggestion 5

def main():
	n = int(input())
	if n % 10 == 7:
		print("Yes")
	elif n // 10 % 10 == 7:
		print("Yes")
	elif n // 100 % 10 == 7:
		print("Yes")

=======
Suggestion 6

def judge(n):
    if n % 10 == 7:
        return True
    elif n >= 10:
        return judge(n // 10)
    else:
        return False

=======
Suggestion 7

def isContainSeven(num):
    if num % 10 == 7 or num // 10 % 10 == 7 or num // 100 == 7:
        return True
    else:
        return False

=======
Suggestion 8

def main():
    # 读取输入
    n = int(input())
    # 判断是否包含数字7
    if n % 10 == 7 or n // 10 % 10 == 7 or n // 100 == 7:
        print("Yes")

=======
Suggestion 9

def is_contain_seven(n):
    if n % 10 == 7:
        return True
    elif n // 10 == 7:
        return True
    elif n // 100 == 7:
        return Tru

=======
Suggestion 10

def main():
    N = int(input())
    if N%10==7 or N//10%10==7 or N//100%10==7:
        print("Yes")
    else:
        print("No")
