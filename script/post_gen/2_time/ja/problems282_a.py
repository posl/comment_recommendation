Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    print(''.join([chr(ord('A') + i) for i in range(K)]))

=======
Suggestion 2

def main():
    K = int(input())
    print("".join([chr(ord("A") + i) for i in range(K)]))

=======
Suggestion 3

def main():
    k = int(input())
    print("".join([chr(ord("A") + i) for i in range(k)]))

=======
Suggestion 4

def main():
    K = int(input())
    print("".join([chr(ord('A') + i) for i in range(K)]))

=======
Suggestion 5

def main():
    n = int(input())
    ans = ''
    for i in range(n):
        ans += chr(ord('A') + i)
    print(ans)

=======
Suggestion 6

def main():
    K = int(input())
    print("".join([chr(i) for i in range(65, 65 + K)]))

=======
Suggestion 7

def main():
    k = int(input())
    for i in range(65, 65+k):
        print(chr(i), end='')

=======
Suggestion 8

def main():
    k = int(input())
    print(''.join([chr(i+65) for i in range(k)]))
