Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    print(chr(65 + (x - 1) % 26))

=======
Suggestion 2

def main():
    n,x = map(int,input().split())
    if x <= n:
        print(chr(x + ord('A') - 1))
    else:
        print(chr((x - n - 1) % 26 + ord('A')))
main()

=======
Suggestion 3

def get_char(n,x):
    char_list = []
    for i in range(65,91):
        char_list.append(chr(i)*n)
    char_str = ''.join(char_list)
    return char_str[x-1]

=======
Suggestion 4

def main():
    x = input()
    n = int(x.split()[0])
    x = int(x.split()[1])
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(alphabet[(x-1)//n])

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    print(chr(64 + int((x - 1) / n + 1)))

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    if x % n == 0:
        print(chr(x // n + 64))
    else:
        print(chr(x // n + 65))

=======
Suggestion 7

def main():
    N,X = map(int, input().split())
    print(chr(ord('A') + (X - 1) % 26))

=======
Suggestion 8

def problems257_a():
    pass

=======
Suggestion 9

def problems257_a(n,x):
    #n=1
    #x=3
    #n=2
    #x=12
    #n=3
    #x=27
    #n=4
    #x=52
    #n=5
    #x=80
    #n=6
    #x=111
    #n=7
    #x=145
    #n=8
    #x=182
    #n=9
    #x=222
    #n=10
    #x=265
    #n=11
    #x=311
    #n=12
    #x=360
    #n=13
    #x=412
    #n=14
    #x=467
    #n=15
    #x=525
    #n=16
    #x=586
    #n=17
    #x=650
    #n=18
    #x=717
    #n=19
    #x=787
    #n=20
    #x=860
    #n=21
    #x=936
    #n=22
    #x=1015
    #n=23
    #x=1097
    #n=24
    #x=1182
    #n=25
    #x=1270
    #n=26
    #x=1361
    #n=27
    #x=1455
    #n=28
    #x=1552
    #n=29
    #x=1652
    #n=30
    #x=1755
    #n=31
    #x=1861
    #n=32
    #x=1970
    #n=33
    #x=2082
    #n=34
    #x=2197
    #n=35
    #x=2315
    #n=36
    #x=2436
    #n=37
    #x=2560
    #n=38
    #x=2687
    #n=39
    #x=2817
    #n=40
    #

=======
Suggestion 10

def get_char_from_string(n, x):
    if n == 1:
        return chr(64+x)
    else:
        return chr(64+((x-1)%26)+1)
