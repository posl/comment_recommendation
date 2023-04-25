Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N < 10:
        print("000"+str(N))
    elif N < 100:
        print("00"+str(N))
    elif N < 1000:
        print("0"+str(N))
    else:
        print(N)

=======
Suggestion 2

def main():
    N = int(input())
    print(str(N).zfill(4))

=======
Suggestion 3

def main():
    N = int(input())
    print("{0:04d}".format(N))

main()

=======
Suggestion 4

def main():
    n = int(input())
    print(str(n).zfill(4))

=======
Suggestion 5

def main():
    n = int(input())
    print("{:04d}".format(n))

main()

=======
Suggestion 6

def main():
    n = int(input())
    print('{0:04d}'.format(n))

=======
Suggestion 7

def main():
    n = int(input())
    print("{:04d}".format(n))

=======
Suggestion 8

def main():
    N = int(input())
    print('{:04d}'.format(N))

=======
Suggestion 9

def main():
    print(input().zfill(4))

main()
