Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if n >= 42:
        print("AGC" + str(n + 1).zfill(3))
    else:
        print("AGC" + str(n).zfill(3))

=======
Suggestion 2

def main():
    n = int(input())
    if n > 42:
        print(f'AGC{str(n+1).zfill(3)}')
    else:
        print(f'AGC{str(n).zfill(3)}')

=======
Suggestion 3

def main():
    n = int(input())
    if n <= 54:
        print("AGC" + str(n).zfill(3))
    else:
        print("AGC" + str(n+1).zfill(3))

=======
Suggestion 4

def main():
    N = int(input())
    if N < 54:
        print("AGC" + str(N).zfill(3))
    else:
        print("AGC" + str(N + 1).zfill(3))

main()

=======
Suggestion 5

def main():
    n = int(input())
    if n < 43:
        print("AGC{:03d}".format(n))
    else:
        print("AGC{:03d}".format(n + 1))

=======
Suggestion 6

def main():
    n = int(input())
    if n >= 42:
        print('AGC' + str(n + 1).rjust(3, '0'))
    else:
        print('AGC' + str(n).rjust(3, '0'))

=======
Suggestion 7

def main():
    n = int(input())
    if n >= 42:
        print("AGC" + str(n+1))
    else:
        print("AGC" + str(n).zfill(3))

=======
Suggestion 8

def agc(n):
    if n < 43:
        return 'AGC' + str(n).zfill(3)
    else:
        return 'AGC' + str(n+1).zfill(3)

=======
Suggestion 9

def AGC(N):
    if N < 43:
        return "AGC" + str(N).zfill(3)
    else:
        return "AGC" + str(N+1).zfill(3)

N = int(input())
print(AGC(N))

=======
Suggestion 10

def main():
    n = int(input())
    if n >= 43:
        print("AGC0" + str(n+1))
    elif n >= 31:
        print("AGC0" + str(n+2))
    else:
        print("AGC0" + str(n))
