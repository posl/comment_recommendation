Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    p = input().strip().split()
    p = [int(i) for i in p]
    p = [chr(96 + i) for i in p]
    print(''.join(p))

=======
Suggestion 2

def main():
    #p = list(map(int, input().split()))
    p = list(map(int, '5 11 12 16 25 17 18 1 7 10 4 23 20 3 2 24 26 19 14 9 6 22 8 13 15 21'.split()))
    s = [chr(96 + i) for i in p]
    print(''.join(s))

=======
Suggestion 3

def main():
    p = list(map(int,input().split()))
    s = ''
    for i in range(26):
        s += chr(p[i]+96)
    print(s)

=======
Suggestion 4

def problem218_b():
    p = list(map(int, input().split()))
    s = ''
    for i in p:
        s += chr(i + 96)
    print(s)

=======
Suggestion 5

def main():
    p = list(map(int, input().split()))
    s = [chr(ord('a') + p[i] - 1) for i in range(26)]
    print(''.join(s))

=======
Suggestion 6

def main():
    input = raw_input()
    input = input.split()
    for i in range(26):
        input[i] = int(input[i])
    result = ''
    for i in range(26):
        result += chr(input[i]+96)
    print result

=======
Suggestion 7

def main():
    p = list(map(int, input().split()))
    # print(p)
    # print(p.index(1))
    # print(chr(97))
    # print(ord('a'))
    # print(chr(97+1))
    # print(chr(97+2))
    # print(chr(97+25))
    # print(chr(97+26))
    # print(chr(97+27))
    # print(chr(97+28))
    # print(chr(97+29))
    # print(chr(97+30))
    # print(chr(97+31))
    # print(chr(97+32))
    # print(chr(97+33))
    # print(chr(97+34))
    # print(chr(97+35))
    # print(chr(97+36))
    # print(chr(97+37))
    # print(chr(97+38))
    # print(chr(97+39))
    # print(chr(97+40))
    # print(chr(97+41))
    # print(chr(97+42))
    # print(chr(97+43))
    # print(chr(97+44))
    # print(chr(97+45))
    # print(chr(97+46))
    # print(chr(97+47))
    # print(chr(97+48))
    # print(chr(97+49))
    # print(chr(97+50))
    # print(chr(97+51))
    # print(chr(97+52))
    # print(chr(97+53))
    # print(chr(97+54))
    # print(chr(97+55))
    # print(chr(97+56))
    # print(chr(97+57))
    # print(chr(97+58))
    # print(chr(97+59))
    # print(chr(97+60))
    # print(chr(97+61))
    # print(chr(97+62))
    # print(chr(97+63))
    # print(chr(97+64))
    # print(chr(97+65))
    # print(chr(97+66))
    # print(chr(97+67))
    # print(chr(97+68))
    # print(chr(97+69))
    # print(chr(97+70))
    # print(chr(97+71))
    # print(chr(97+72))
    # print(chr(97+73))

=======
Suggestion 8

def print_alphabet(P):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in P:
        result += alphabet[i-1]
    return result

=======
Suggestion 9

def main():
    p = list(map(int, input().split()))
    ans = []
    for i in range(26):
        ans.append(chr(ord('a') + p[i] - 1))
    print(''.join(ans))

=======
Suggestion 10

def main():
    P = list(map(int, input().split()))
    S = [chr(ord('a') + P[i] - 1) for i in range(26)]
    print(''.join(S))
