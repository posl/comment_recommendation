Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N < 42:
        print("AGC" + str(N).zfill(3))
    else:
        print("AGC" + str(N + 1).zfill(3))

=======
Suggestion 2

def main():
    N = int(input())
    if N < 42:
        print('AGC' + str(N).zfill(3))
    else:
        print('AGC' + str(N + 1).zfill(3))

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
    N = int(input())
    if N < 42:
        print("AGC{:03d}".format(N))
    else:
        print("AGC{:03d}".format(N+1))

=======
Suggestion 5

def main():
    n = int(input())
    if n <= 42:
        print('AGC' + str(n).zfill(3))
    else:
        print('AGC' + str(n+1).zfill(3))

=======
Suggestion 6

def main():
    N = int(input())
    if N < 42:
        print("AGC{:03}".format(N))
    else:
        print("AGC{:03}".format(N+1))

=======
Suggestion 7

def main():
    N = int(input())
    if N <= 54:
        print("AGC{:0=3}".format(N+1))
    else:
        print("AGC{:0=3}".format(N))

=======
Suggestion 8

def main():
    n = int(input())
    if n < 42:
        print('AGC{:03}'.format(n))
    else:
        print('AGC{:02}'.format(n + 1))

=======
Suggestion 9

def main():
    n = int(input())
    print("AGC" + str(n + 1).zfill(3))
