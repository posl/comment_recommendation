Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(65, 65+k)]))

=======
Suggestion 2

def main():
    k = int(input())
    print("".join([chr(ord('A') + i) for i in range(k)]))

=======
Suggestion 3

def main():
    K = int(input())
    print("".join([chr(i) for i in range(ord('A'), ord('A')+K)]))

=======
Suggestion 4

def main():
    k = int(input())
    print("".join([chr(i) for i in range(65,65+k)]))

=======
Suggestion 5

def main():
    K = int(input())
    print("".join(chr(i) for i in range(65, 65+K)))

=======
Suggestion 6

def main():
    n = int(input())
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(s[:n])

=======
Suggestion 7

def main():
    input = int(raw_input())
    print ''.join([chr(i) for i in range(65, 65+input)])

=======
Suggestion 8

def main():
    K = int(input())
    print('ABC' if K < 3 else 'ABD')

main()
