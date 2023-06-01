Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())

    if n >= -2**31 and n <= 2**31-1:
        print("是")
    else:
        print("否")

=======
Suggestion 2

def main():
    n = int(input())
    if n >= (-2**31) and n <= (2**31-1):
        print("是")
    else:
        print("否")

=======
Suggestion 3

def judge(num):
    if -2**31 <= num <= 2**31-1:
        return "是"
    else:
        return "否"

=======
Suggestion 4

def is_int_32(num):
    if num >= -2**31 and num <= 2**31-1:
        print("是")
    else:
        print("否")

=======
Suggestion 5

def main():
    n = int(input())
    if -2**31 <= n and n <= 2**31-1:
        print("是")
    else:
        print("否")

=======
Suggestion 6

def main():
    N = int(input())
    if -2**31 <= N <= 2**31-1:
        print("是")
    else:
        print("否")

=======
Suggestion 7

def main():
    n = int(input())
    if n >= -2**31 and n <= 2**31-1:
        print('是')
    else:
        print('否')

=======
Suggestion 8

def is_in_range(n):
    if -2**31 <= n and n <= 2**31 - 1:
        return True
    else:
        return False
