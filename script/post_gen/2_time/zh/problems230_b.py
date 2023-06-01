Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print("AGC{:03d}".format(n))
    return 0

=======
Suggestion 2

def problem230_a():
    n = int(input())
    if n <= 9:
        print("AGC00"+str(n))
    elif n <= 99:
        print("AGC0"+str(n))
    else:
        print("AGC"+str(n))

=======
Suggestion 3

def main():
    n = int(input())
    if n < 10:
        print("AGC00%d" % n)
    elif n < 100:
        print("AGC0%d" % n)
    else:
        print("AGC%d" % n)

=======
Suggestion 4

def main():
    N = int(input())
    if N < 10:
        print("AGC00" + str(N))
    elif N < 100:
        print("AGC0" + str(N))
    else:
        print("AGC" + str(N))

=======
Suggestion 5

def AGC(n):
    if n < 10:
        return '00' + str(n)
    elif n < 100:
        return '0' + str(n)
    else:
        return str(n)

n = int(input())

=======
Suggestion 6

def problem230_a():
    n = int(input())
    if n < 10:
        print('AGC00' + str(n))
    elif n < 100:
        print('AGC0' + str(n))
    else:
        print('AGC' + str(n))

=======
Suggestion 7

def main():
    N = input()
    if int(N) < 10:
        N = '00' + N
    elif int(N) < 100:
        N = '0' + N
    else:
        N = N
    print('AGC' + N)

=======
Suggestion 8

def main():
    n = int(input())
    if n < 10:
        print("AGC00" + str(n))
    elif n < 100:
        print("AGC0" + str(n))
    else:
        print("AGC" + str(n))

=======
Suggestion 9

def main():
    N = int(input())
    if N <= 9:
        print("AGC00" + str(N))
    elif N <= 99:
        print("AGC0" + str(N))
    else:
        print("AGC" + str(N))
