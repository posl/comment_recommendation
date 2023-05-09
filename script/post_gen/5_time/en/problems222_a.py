Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def leading_zero(num):
    if num < 10:
        return '000' + str(num)
    elif num < 100:
        return '00' + str(num)
    elif num < 1000:
        return '0' + str(num)
    else:
        return str(num)

=======
Suggestion 2

def main():
    n = int(input())
    print('{0:04d}'.format(n))

=======
Suggestion 3

def main():
    n = int(input())
    print('{:04d}'.format(n))

=======
Suggestion 4

def main():
    n = int(input())
    print("{0:04d}".format(n))

=======
Suggestion 5

def main():
    n = input()
    print(n.zfill(4))

=======
Suggestion 6

def main():
    N = input()
    print(N.zfill(4))

=======
Suggestion 7

def main():
    N = input()
    print("{:04d}".format(int(N)))
