Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N < 10:
        print("AGC00" + str(N))
    elif N < 100:
        print("AGC0" + str(N))
    else:
        print("AGC" + str(N))

=======
Suggestion 2

def main():
    n = int(input())
    if n < 10:
        print("AGC00"+str(n))
    elif n < 100:
        print("AGC0"+str(n))
    else:
        print("AGC"+str(n))
    return

=======
Suggestion 3

def main():
    n = int(input())
    if n < 10:
        print("AGC00{}".format(n))
    elif n < 100:
        print("AGC0{}".format(n))
    else:
        print("AGC{}".format(n))

=======
Suggestion 4

def main():
    N = int(input())
    if N <= 9:
        print("AGC00" + str(N))
    elif N <= 99:
        print("AGC0" + str(N))
    else:
        print("AGC" + str(N))

=======
Suggestion 5

def main():
    N = int(input())
    if N <= 9:
        print("AGC00" + str(N))
    elif N <= 99:
        print("AGC0" + str(N))
    else:
        print("AGC" + str(N))

main()

=======
Suggestion 6

def main():
    n = int(input())
    if n <= 21:
        print("AGC{:03d}".format(n))
    else:
        print("AGC{:03d}".format(n+2))

=======
Suggestion 7

def main():
    N = int(input())
    if N <= 21:
        print("AGC0{0}".format(N))
    else:
        print("AGC{0}".format(N))

=======
Suggestion 8

def main():
    N = int(input())
    print("AGC" + str(N).zfill(3))
