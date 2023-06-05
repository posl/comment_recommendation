Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n <= 9:
        print("AGC00"+str(n))
    elif n <= 99:
        print("AGC0"+str(n))
    else:
        print("AGC"+str(n))

=======
Suggestion 2

def get_AGC_name(n):
    if n > 42:
        return 'AGC' + str(n + 1).zfill(3)
    elif n == 42:
        return 'AGC043'
    elif n > 19:
        return 'AGC' + str(n).zfill(3)
    elif n == 19:
        return 'AGC020'
    else:
        return 'AGC' + str(n).zfill(3)

=======
Suggestion 3

def agc(n):
    if n < 10:
        return "00" + str(n)
    elif n < 100:
        return "0" + str(n)
    else:
        return str(n)

=======
Suggestion 4

def main():
    n = int(input())
    if n < 10:
        print('AGC00' + str(n))
    elif n < 100:
        print('AGC0' + str(n))
    else:
        print('AGC' + str(n))

=======
Suggestion 5

def main():
    n = int(input())
    if n <= 9:
        print('AGC00' + str(n))
    elif n <= 99:
        print('AGC0' + str(n))
    else:
        print('AGC' + str(n))

=======
Suggestion 6

def main():
    n = int(input())
    if n >= 1 and n <= 9:
        print('AGC00' + str(n))
    elif n >= 10 and n <= 99:
        print('AGC0' + str(n))
    elif n >= 100 and n <= 999:
        print('AGC' + str(n))

=======
Suggestion 7

def agc(n):
    if n<10:
        print('AGC00'+str(n))
    elif n<100:
        print('AGC0'+str(n))
    else:
        print('AGC'+str(n))

n=int(input())
