Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(65, 65+k)]))

=======
Suggestion 2

def main():
    K = int(input())
    print(''.join([chr(ord('A') + i) for i in range(K)]))

=======
Suggestion 3

def main():
    k = int(input())
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(letters[:k])

=======
Suggestion 4

def main():
    k = int(input())
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(alpha[0:k])

=======
Suggestion 5

def main():
    K = int(input())
    print(''.join([chr(x) for x in range(ord('A'), ord('A') + K)]))

=======
Suggestion 6

def main():
    k = int(input())
    print(''.join([chr(65 + i) for i in range(k)]))

=======
Suggestion 7

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(ord('A'), ord('A') + k)]))

=======
Suggestion 8

def main():
    num = int(input())
    for i in range(num):
        print(chr(ord("A")+i),end="")
    print()
main()

=======
Suggestion 9

def main():
    k=int(input())
    for i in range(k):
        print(chr(i+65),end='')
    print()
