Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n < 10:
        print('000' + str(n))
    elif n < 100:
        print('00' + str(n))
    elif n < 1000:
        print('0' + str(n))
    else:
        print(str(n))

=======
Suggestion 2

def main():
    N = input()
    if len(N) == 1:
        print('000' + N)
    elif len(N) == 2:
        print('00' + N)
    elif len(N) == 3:
        print('0' + N)
    else:
        print(N)

=======
Suggestion 3

def main():
    n = int(input())
    print(str(n).zfill(4))

=======
Suggestion 4

def main():
    n = input()
    print(n.zfill(4))

=======
Suggestion 5

def main():
    n = int(input())
    print('{0:04d}'.format(n))

=======
Suggestion 6

def main():
    N = input()
    print("{:0>4}".format(N))

=======
Suggestion 7

def main():
    n = input()
    print(n.rjust(4, '0'))

=======
Suggestion 8

def main():
    n = input()
    print(n.zfill(4))
    return

=======
Suggestion 9

def main():
    N = int(input())
    print('{:04d}'.format(N))
    return
