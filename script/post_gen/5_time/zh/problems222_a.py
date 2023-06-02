Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #从标准输入读取整数
    n = int(input())
    #格式化输出
    print('{:04d}'.format(n))

=======
Suggestion 2

def test():
    N = input()
    N = int(N)
    if N < 0 or N > 9999:
        return
    print("%04d" % N)

=======
Suggestion 3

def add_zero(n):
    if n < 10:
        return '000' + str(n)
    elif n < 100:
        return '00' + str(n)
    elif n < 1000:
        return '0' + str(n)
    else:
        return str(n)

n = int(input())
print(add_zero(n))

=======
Suggestion 4

def main():
    N = int(input())
    print("{:04d}".format(N))

=======
Suggestion 5

def main():
    n = int(input())
    print('{:0>4}'.format(n))

=======
Suggestion 6

def main():
    n = input()
    print('{:0>4}'.format(n))

=======
Suggestion 7

def main():
    n = int(input())
    print(f"{n:04d}")

=======
Suggestion 8

def main():
    n = int(input())
    print("%04d" % n)
    # print('{0:04d}'.format(n))
    # print('{:04d}'.format(n))
    # print(f"{n:04d}")
    # print(f"{n:0>4}")
    # print(format(n, '04d'))
    # print(format(n, '0>4'))
    # print(format(n, '04'))
    # print(format(n, '0>4'))
    # print(format(n, '04d'))
    # print(format(n, '0>4d'))
    # print(format(n, '04d'))
    # print(format(n, '0>4d'))
    # print(format(n, '04d'))
    # print(format(n, '0>4d'))
    # print(format(n, '04d'))
    # print(format(n, '0>4d'))
    # print(format(n, '04d'))
    # print(format(n, '0>4d'))
    # print(format(n, '04d'))
    # print(format(n, '0>4d'))
    # print(format(n, '04d'))
    # print(format(n, '0>4d'))
    # print(format(n, '04d'))
    # print(format(n, '0>4d'))
    # print(format(n, '04d'))
    # print(format(n, '0>4d'))

=======
Suggestion 9

def main():
    a = int(input())
    print('{:0=4}'.format(a))
main()

=======
Suggestion 10

def add_zero(num):
    num_str = str(num)
    while len(num_str) < 4:
        num_str = "0" + num_str
    return num_str

print(add_zero(int(input())))
