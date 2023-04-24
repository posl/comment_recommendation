Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n < 10:
        print("000" + str(n))
    elif n < 100:
        print("00" + str(n))
    elif n < 1000:
        print("0" + str(n))
    else:
        print(str(n))

=======
Suggestion 2

def main():
    n = input()
    if len(n) == 1:
        print("000"+n)
    elif len(n) == 2:
        print("00"+n)
    elif len(n) == 3:
        print("0"+n)
    else:
        print(n)

=======
Suggestion 3

def main():
    N = int(input())
    print('{:04d}'.format(N))

=======
Suggestion 4

def main():
    n = input()
    print(n.zfill(4))

=======
Suggestion 5

def main():
    n = int(input())
    print('{0:0=4d}'.format(n))

=======
Suggestion 6

def main():
    # Take input Here and Call solution function
    n = int(input())
    print(solution(n))

=======
Suggestion 7

def main():
    n = input()
    print(n.zfill(4))
    return
