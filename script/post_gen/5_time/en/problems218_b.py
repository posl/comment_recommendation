Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    p = list(map(int, input().split()))
    s = [None] * 26
    for i in range(26):
        s[p[i]-1] = chr(97+i)
    print("".join(s))

=======
Suggestion 2

def main():
    p = list(map(int, input().split()))
    alphabets = [chr(ord('a') + i - 1) for i in p]
    print(''.join(alphabets))

=======
Suggestion 3

def main():
    # input
    P = list(map(int, input().split()))

    # compute

    # output
    print(''.join([chr(ord('a') + P[i] - 1) for i in range(26)]))

=======
Suggestion 4

def main():
    p = list(map(int,input().split()))
    alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
    for i in range(26):
        print(alpha[p[i]-1],end='')
    print()

=======
Suggestion 5

def main():
    p = [int(x) for x in input().split()]
    print(''.join([chr(ord('a') + x - 1) for x in p]))

=======
Suggestion 6

def main():
    p = list(map(int, input().split()))
    s = [chr(p[i] + 96) for i in range(len(p))]
    print(''.join(s))

=======
Suggestion 7

def main():
    p = list(map(int, input().split()))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(p)):
        print(alphabet[p[i]-1], end='')

=======
Suggestion 8

def get_alphabet():
    p = input().split()
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    for i in range(26):
        alphabet[int(p[i])-1] = chr(i+ord('a'))
    print(''.join(alphabet))

get_alphabet()

=======
Suggestion 9

def main():
    input_list = list(map(int, input().split()))
    alpha_list = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(26):
        print(alpha_list[input_list[i]-1], end='')

=======
Suggestion 10

def main():
    print("abcdefghijklmnopqrstuvwxyz")
