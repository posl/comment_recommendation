Synthesizing 10/10 solutions

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
    n = int(input())
    if n < 42:
        print('AGC' + str(n).zfill(3))
    else:
        print('AGC' + str(n + 1).zfill(3))

=======
Suggestion 3

def main():
    N = int(input())
    if N < 42:
        print("AGC{:03d}".format(N))
    else:
        print("AGC{:03d}".format(N+1))

=======
Suggestion 4

def main():
    n = int(input())
    if n < 42:
        print("AGC{0:03d}".format(n))
    else:
        print("AGC{0:03d}".format(n+1))

=======
Suggestion 5

def main():
    n = int(input())
    if n >= 42:
        print("AGC"+str(n+1).zfill(3))
    else:
        print("AGC"+str(n).zfill(3))

=======
Suggestion 6

def main():
    N = int(input())
    if N >= 42:
        print("AGC{:03}".format(N+1))
    else:
        print("AGC{:03}".format(N))

=======
Suggestion 7

def main():
    N = int(input())
    if N < 41:
        print("AGC%03d" % N)
    elif N < 54:
        print("AGC%03d" % (N + 1))
    else:
        print("AGC054")

=======
Suggestion 8

def main():
    n = int(input())
    if n <= 54:
        print("AGC" + str(n + 1).zfill(3))
    else:
        print("AGC" + str(n + 2).zfill(3))

=======
Suggestion 9

def main():
    n = int(input())
    if n <= 54:
        print("AGC"+str(n+1).zfill(3))
    else:
        print("AGC055")

=======
Suggestion 10

def main():
    n = int(input())
    if n <= 54:
        print("AGC" + str(n + 100)[1:])
    else:
        print("AGC" + str(n + 1000)[1:])
main()
