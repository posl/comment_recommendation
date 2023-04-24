Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = input()
    if len(N) == 1:
        print('000'+N)
    elif len(N) == 2:
        print('00'+N)
    elif len(N) == 3:
        print('0'+N)
    else:
        print(N)

=======
Suggestion 2

def main():
    n = input()
    if len(n) == 4:
        print(n)
    elif len(n) == 3:
        print("0" + n)
    elif len(n) == 2:
        print("00" + n)
    elif len(n) == 1:
        print("000" + n)

=======
Suggestion 3

def main():
    n = int(input())
    print(str(n).zfill(4))

=======
Suggestion 4

def main():
    #入力
    N = int(input())
    #処理
    N = str(N)
    N = N.zfill(4)
    #出力
    print(N)

=======
Suggestion 5

def main():
    N = int(input())
    print("{0:04d}".format(N))

=======
Suggestion 6

def main():
    n = int(input())
    print("{0:04d}".format(n))

=======
Suggestion 7

def main():
    n = int(input())
    print("{:04d}".format(n))

=======
Suggestion 8

def main():
    N = int(input())
    print(format(N, '04d'))

=======
Suggestion 9

def main():
    N = int(input())
    print('{0:04}'.format(N))

=======
Suggestion 10

def main():
    N = int(input())
    print(format(N, "04d"))
