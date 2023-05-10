Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    print(n.zfill(4))

=======
Suggestion 2

def main():
    n = int(input())
    n = str(n)
    while len(n) < 4:
        n = "0" + n
    print(n)

=======
Suggestion 3

def main():
    n = int(input())
    print("%04d" % n)

=======
Suggestion 4

def main():
    N = input()
    print(N.zfill(4))

=======
Suggestion 5

def main():
    N = int(input())
    print("{:04}".format(N))
