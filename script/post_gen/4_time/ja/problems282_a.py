Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    ans = ""
    for i in range(k):
        ans += chr(ord('A') + i)
    print(ans)

=======
Suggestion 2

def main():
    k = int(input())
    print(''.join([chr(ord('A') + i) for i in range(k)]))

=======
Suggestion 3

def main():
    K = int(input())
    alphabets = [chr(i) for i in range(65, 65+26)]
    print(''.join(alphabets[:K]))

=======
Suggestion 4

def main():
    k = int(input())
    print("".join([chr(i) for i in range(65, 65 + k)]))

=======
Suggestion 5

def main():
    k = int(input())
    ans = ""
    for i in range(k):
        ans += chr(i+ord("A"))
    print(ans)

=======
Suggestion 6

def main():
    k = int(input().strip())
    print(''.join([chr(ord('A') + i) for i in range(k)]))

=======
Suggestion 7

def main():
    n = int(input())
    print(''.join([chr(i) for i in range(65, 65+n)]))

=======
Suggestion 8

def main():
    # input
    k = int(input())

    # compute

    # output
    print('ABC'[:k])

=======
Suggestion 9

def main():
    k = int(input())
    print("".join(list(map(chr, range(65, 65+k)))))

=======
Suggestion 10

def main():
    K = int(input())
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(a[:K])
