Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if n < 10:
        print("AGC00"+str(n))
    elif n < 100:
        print("AGC0"+str(n))
    else:
        print("AGC"+str(n))

=======
Suggestion 2

def main():
    N = int(input())
    if N < 10:
        print("AGC00"+str(N))
    elif N < 100:
        print("AGC0"+str(N))
    else:
        print("AGC"+str(N))

=======
Suggestion 3

def main():
    n = int(input())
    if n < 42:
        print("AGC" + str(n).zfill(3))
    else:
        print("AGC" + str(n + 1).zfill(3))

=======
Suggestion 4

def main():
    n = int(input())
    if n < 42:
        print("AGC{:03d}".format(n))
    else:
        print("AGC{:03d}".format(n+1))

=======
Suggestion 5

def main():
    n = int(input())
    if n < 42:
        print("AGC{:0=3}".format(n))
    else:
        print("AGC{:0=3}".format(n+1))

=======
Suggestion 6

def main():
    N = int(input())
    if N < 42:
        print("AGC{:0=3}".format(N))
    else:
        print("AGC{:0=3}".format(N+1))

=======
Suggestion 7

def main():
    N = int(input())
    if N < 42:
        print("AGC{}".format(str(N).zfill(3)))
    else:
        print("AGC{}".format(str(N+1).zfill(3)))

=======
Suggestion 8

def main():
    n = int(input())
    if n >= 42:
        print('AGC'+str(n+1).zfill(3))
    else:
        print('AGC'+str(n).zfill(3))

=======
Suggestion 9

def main():
    n = int(input())
    if n < 42:
        print('AGC' + '{:0=3}'.format(n))
    else:
        print('AGC' + '{:0=3}'.format(n+1))

=======
Suggestion 10

def main():
    n = int(input())
    if n < 42:
        print('AGC{:0>3}'.format(n))
    else:
        print('AGC{:0>3}'.format(n+1))
