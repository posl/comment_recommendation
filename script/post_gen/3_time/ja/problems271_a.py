Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print('{:02X}'.format(N))

=======
Suggestion 2

def main():
    n = int(input())
    print("{:02X}".format(n))

=======
Suggestion 3

def main():
    #入力
    n = int(input())
    #16進数に変換
    n = hex(n)
    #先頭の0xを削除
    n = n[2:]
    #出力
    print(n.upper().zfill(2))

=======
Suggestion 4

def main():
    N = int(input())
    print(format(N, '02X'))

=======
Suggestion 5

def main():
    N = int(input())
    print("{:02x}".format(N).upper())

=======
Suggestion 6

def main():
    #入力
    n = int(input())
    #出力
    print("{0:02X}".format(n))

=======
Suggestion 7

def main():
    N = input()
    print('{:0>2}'.format(hex(int(N))[2:].upper()))

=======
Suggestion 8

def main():
    N = int(input())

    print("{0:02X}".format(N))
