Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N < 42:
        print("AGC{:0=3}".format(N))
    else:
        print("AGC{:0=3}".format(N+1))

=======
Suggestion 2

def main():
    n = int(input())
    if n < 42:
        print("AGC" + str(n).zfill(3))
    else:
        print("AGC" + str(n+1).zfill(3))

=======
Suggestion 3

def main():
    n = int(input())
    if n < 42:
        print('AGC{:0=3}'.format(n))
    else:
        print('AGC{:0=3}'.format(n+1))

=======
Suggestion 4

def main():
    N = int(input())
    if N < 42:
        print("AGC{:03d}".format(N))
    else:
        print("AGC{:03d}".format(N+1))

=======
Suggestion 5

def main():
    n = int(input())
    if n < 10:
        print("AGC00" + str(n))
    elif n < 100:
        print("AGC0" + str(n))
    else:
        print("AGC" + str(n))

=======
Suggestion 6

def main():
    n = int(input())
    if n < 10:
        print("AGC00" + str(n))
    elif n >= 10 and n < 100:
        print("AGC0" + str(n))
    else:
        print("AGC" + str(n))

=======
Suggestion 7

def main():
    N = int(input())
    if N < 42:
        print("AGC%03d" % N)
    else:
        print("AGC%03d" % (N+1))

=======
Suggestion 8

def main():
    n = int(input())
    if n < 42:
        print("AGC{:03d}".format(n))
    else:
        print("AGC{:03d}".format(n+1))
