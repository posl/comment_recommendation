Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    if len(n) == 1:
        print("000" + n)
    elif len(n) == 2:
        print("00" + n)
    elif len(n) == 3:
        print("0" + n)
    else:
        print(n)

=======
Suggestion 2

def main():
    N = int(input())
    if N < 10:
        print("000" + str(N))
    elif N < 100:
        print("00" + str(N))
    elif N < 1000:
        print("0" + str(N))
    else:
        print(N)

=======
Suggestion 3

def main():
    n = input()
    print(n.zfill(4))

=======
Suggestion 4

def main():
    N = input()
    print(N.zfill(4))

=======
Suggestion 5

def main():
    N = input()
    N = N.zfill(4)
    print(N)

=======
Suggestion 6

def main():
    N = int(input())
    print("{:04d}".format(N))

=======
Suggestion 7

def main():
    n = int(input())
    print('{:04d}'.format(n))

=======
Suggestion 8

def main():
    n = int(input())
    print("{:04}".format(n))
