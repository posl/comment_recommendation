Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(ord('A'), ord('A') + K)]))

=======
Suggestion 2

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(65, 65+k)]))

=======
Suggestion 3

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(65, 65+K)]))

=======
Suggestion 4

def main():
    K = int(input())
    print("".join([chr(i) for i in range(65, 65+K)]))

=======
Suggestion 5

def main():
    k = int(input())
    print(''.join([chr(ord('A')+i) for i in range(k)]))

=======
Suggestion 6

def main():
    k = int(input())
    print(''.join(chr(i) for i in range(65, 65+k)))

=======
Suggestion 7

def main():
    k = int(input())
    for i in range(k):
        print(chr(ord('A')+i),end='')
    print()

=======
Suggestion 8

def main():
    K = int(input())
    print("ABC"[:K])
