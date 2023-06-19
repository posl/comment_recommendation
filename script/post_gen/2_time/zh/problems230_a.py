Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n <= 9:
        print('AGC00'+str(n))
    elif n <= 99:
        print('AGC0'+str(n))
    else:
        print('AGC'+str(n))

=======
Suggestion 2

def main():
    n = int(input())
    if n >= 1 and n <= 9:
        print('AGC00' + str(n))
    elif n >= 10 and n <= 99:
        print('AGC0' + str(n))
    else:
        print('AGC' + str(n))

=======
Suggestion 3

def main():
    N = int(input())
    if N >= 43:
        print("AGC{:03d}".format(N+1))
    elif N >= 20:
        print("AGC{:03d}".format(N))
    else:
        print("AGC{:03d}".format(N))

=======
Suggestion 4

def main():
    n = int(input())
    if n <= 9:
        print("AGC00" + str(n))
    elif n <= 99:
        print("AGC0" + str(n))
    else:
        print("AGC" + str(n))

=======
Suggestion 5

def main():
    n=int(input())
    if n<=21:
        print("AGC0"+str(n))
    else:
        print("AGC"+str(n+1))

=======
Suggestion 6

def main():
    N = int(input())
    if N <= 9:
        print("AGC00" + str(N))
    elif N >= 10 and N <= 99:
        print("AGC0" + str(N))
    else:
        print("AGC" + str(N))

main()

=======
Suggestion 7

def main():
    n = int(input())
    if n < 10:
        print("AGC00"+str(n))
    elif n < 100:
        print("AGC0"+str(n))
    else:
        print("AGC"+str(n))

=======
Suggestion 8

def main():
    n = int(input())
    if n < 10:
        print('AGC00'+str(n))
    elif n < 100:
        print('AGC0'+str(n))
    else:
        print('AGC'+str(n))
