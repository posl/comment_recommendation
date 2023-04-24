Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n < 10:
        print("AGC00" + str(n))
    elif n < 100:
        print("AGC0" + str(n))
    else:
        print("AGC" + str(n))

=======
Suggestion 2

def main():
    N = int(input())
    if N < 10:
        print("AGC00" + str(N))
    elif N < 100:
        print("AGC0" + str(N))
    else:
        print("AGC" + str(N))
    return

=======
Suggestion 3

def main():
    N = int(input())
    if N < 10:
        print("AGC00"+str(N))
    elif N < 100:
        print("AGC0"+str(N))
    else:
        print("AGC"+str(N))

=======
Suggestion 4

def main():
    N = int(input())
    if N >= 1 and N <= 9:
        print("AGC00" + str(N))
    elif N >= 10 and N <= 99:
        print("AGC0" + str(N))
    elif N >= 100 and N <= 999:
        print("AGC" + str(N))

=======
Suggestion 5

def main():
    N = int(input())
    if N <= 9:
        print('AGC00{}'.format(N))
    elif N <= 99:
        print('AGC0{}'.format(N))
    else:
        print('AGC{}'.format(N))

=======
Suggestion 6

def main():
    N = int(input())
    if N < 10:
        print("AGC00"+str(N))
    elif N >= 10 and N < 100:
        print("AGC0"+str(N))
    else:
        print("AGC"+str(N))

=======
Suggestion 7

def main():
    N = int(input())
    if N <= 21:
        print('AGC' + str(N).zfill(3))
    else:
        print('AGC' + str(N+1).zfill(3))

=======
Suggestion 8

def main():
    n = int(input())
    if n <= 21:
        print('AGC'+str(100+n)[1:])
    else:
        print('AGC'+str(100+n+1)[1:])

=======
Suggestion 9

def get_agc(n):
    if n <= 21:
        return 'AGC%03d' % (n + 2)
    else:
        return 'AGC%03d' % (n + 1)

print(get_agc(int(input())))
