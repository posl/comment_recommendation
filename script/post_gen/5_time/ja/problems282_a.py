Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    print('ABC'[:k])

=======
Suggestion 2

def main():
    K = int(input())
    print("".join([chr(i) for i in range(65, 65+K)]))

=======
Suggestion 3

def main():
    k = int(input())
    a = ord('A')
    for i in range(k):
        print(chr(a+i), end="")
    print()

=======
Suggestion 4

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(65, 65+k)]))

=======
Suggestion 5

def main():
    k = int(input())
    ans = ''
    for i in range(k):
        ans += chr(65+i)
    print(ans)

=======
Suggestion 6

def main():
    k = int(input())
    print("".join([chr(i) for i in range(65, 65+k)]))

=======
Suggestion 7

def main():
    K = int(input())
    print('ABC'*K)

=======
Suggestion 8

def main():
    K = int(input())
    print(''.join([chr(ord('A') + i) for i in range(K)]))

=======
Suggestion 9

def main():
    k = int(input())
    print("ABC"[:k])
