Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    if len(n) == 1:
        print("000" + n)
    elif len(n) == 2:
        print("00" + n)
    elif len(n) == 3:
        print("0" + n)
    else:
        print(n)

=======
Suggestion 2

def main():
    # input
    N = input()
    # solve
    if len(N) == 4:
        print(N)
    elif len(N) == 3:
        print("0"+N)
    elif len(N) == 2:
        print("00"+N)
    else:
        print("000"+N)

=======
Suggestion 3

def main():
    # input
    N = input()
    # compute
    ans = '0'*(4-len(N))+N
    # output
    print(ans)

=======
Suggestion 4

def main():
    n = input()
    print(n.zfill(4))

=======
Suggestion 5

def main():
    N = input()
    print(N.zfill(4))

=======
Suggestion 6

def main():
    N = input()
    print('{:0>4}'.format(N))

=======
Suggestion 7

def main():
    num = input()
    print(num.zfill(4))
