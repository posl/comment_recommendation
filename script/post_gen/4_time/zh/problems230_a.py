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
    print('AGC%03d' % (N if N < 43 else N - 1))

=======
Suggestion 3

def main():
    n = int(input())
    if n < 10:
        print('AGC' + '00' + str(n))
    elif n < 100:
        print('AGC' + '0' + str(n))
    else:
        print('AGC' + str(n))

main()

=======
Suggestion 4

def main():
    n = int(input())
    if n < 10:
        n = '00' + str(n)
    elif n < 100:
        n = '0' + str(n)
    else:
        n = str(n)
    if n[1:] == '00':
        print('AGC' + n[0])
    elif n[1:] == '01':
        print('AGC' + n[0])
    elif n[1:] == '02':
        print('AGC' + n[0])
    elif n[1:] == '03':
        print('AGC' + n[0])
    elif n[1:] == '04':
        print('AGC' + n[0])
    elif n[1:] == '05':
        print('AGC' + n[0])
    elif n[1:] == '06':
        print('AGC' + n[0])
    elif n[1:] == '07':
        print('AGC' + n[0])
    elif n[1:] == '08':
        print('AGC' + n[0])
    elif n[1:] == '09':
        print('AGC' + n[0])
    elif n[1:] == '10':
        print('AGC' + n[0])
    elif n[1:] == '11':
        print('AGC' + n[0])
    elif n[1:] == '12':
        print('AGC' + n[0])
    elif n[1:] == '13':
        print('AGC' + n[0])
    elif n[1:] == '14':
        print('AGC' + n[0])
    elif n[1:] == '15':
        print('AGC' + n[0])
    elif n[1:] == '16':
        print('AGC' + n[0])
    elif n[1:] == '17':
        print('AGC' + n[0])
    elif n[1:] == '18':
        print('AGC' + n[0])
    elif n[1:] == '19':
        print('AGC' + n[0])
    elif n[1:] == '20':
        print('AGC' + n[0])
    elif n[1:] == '

=======
Suggestion 5

def problem230_a():
    n = int(input())
    if n < 10:
        print("AGC00" + str(n))
    elif n < 100:
        print("AGC0" + str(n))
    else:
        print("AGC" + str(n))

problem230_a()

=======
Suggestion 6

def main():
    n = int(input())
    if n <= 21:
        print("AGC0" + str(n-1))
    else:
        print("AGC" + str(n-1))

=======
Suggestion 7

def main():
    N = int(input())
    if N <= 21:
        print('AGC' + str(100 + N)[1:4])
    else:
        print('AGC' + str(100 + N + 1)[1:4])
