Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    # print(k)
    # print(type(k))
    if k >= 1 and k <= 26:
        for i in range(0,k):
            print(chr(65+i),end="")
        print()
    else:
        print("K is out of range.")
        return 0

=======
Suggestion 2

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(ord('A'), ord('A') + k)]))

=======
Suggestion 3

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(65,65+K)]))

=======
Suggestion 4

def main():
    K = int(input())
    print(''.join([chr(x) for x in range(65, 65 + K)]))

=======
Suggestion 5

def main():
    k = int(input())
    s = ''
    for i in range(k):
        s += chr(65+i)
    print(s)

=======
Suggestion 6

def main():
    k = int(input())
    for i in range(k):
        print(chr(65 + i), end='')
    print()

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(0, n):
        print(chr(ord('A') + i), end='')
    print()

=======
Suggestion 8

def main():
    k = int(input())
    print("".join([chr(i) for i in range(65, 65+k)]))

=======
Suggestion 9

def main():
    k = int(input())
    for i in range(k):
        print(chr(ord('A')+i),end="")
    print()
