Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = input()
    if len(N) == 4:
        print(N)
    elif len(N) == 3:
        print("0" + N)
    elif len(N) == 2:
        print("00" + N)
    elif len(N) == 1:
        print("000" + N)

=======
Suggestion 2

def main():
    num = input()
    if len(num) == 1:
        print("000" + num)
    elif len(num) == 2:
        print("00" + num)
    elif len(num) == 3:
        print("0" + num)
    else:
        print(num)

=======
Suggestion 3

def main():
    N = int(input())
    print(str(N).zfill(4))

=======
Suggestion 4

def main():
    N = int(input())
    print("{0:04d}".format(N))

=======
Suggestion 5

def main():
    n = int(input())
    print("{:04d}".format(n))

main()

=======
Suggestion 6

def main():
    N = int(input())
    print('{0:04d}'.format(N))

=======
Suggestion 7

def main():
    n = int(input())
    print('{0:04d}'.format(n))

=======
Suggestion 8

def main():
    N = int(input())
    print(format(N, '04d'))

=======
Suggestion 9

def main():
    N = int(input())
    print('{:04}'.format(N))
