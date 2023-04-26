Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    print(''.join([chr(ord('A') + i) for i in range(k)]))

=======
Suggestion 2

def main():
    K = int(input())
    ans = ""
    for i in range(K):
        ans += chr(65+i)
    print(ans)

=======
Suggestion 3

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(ord('A'), ord('A') + K)]))

=======
Suggestion 4

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(65, 65+K)]))

=======
Suggestion 5

def main():
    K = int(input())
    print("".join([chr(i) for i in range(65,65+K)]))

=======
Suggestion 6

def main():
    k = int(input())
    s = ""
    for i in range(k):
        s += chr(i + 65)
    print(s)

=======
Suggestion 7

def main():
    K = int(input())
    print(''.join(chr(ord('A')+i) for i in range(K)))

=======
Suggestion 8

def main():
    #input
    k = int(input())
    #output
    print(''.join([chr(i) for i in range(65,65+k)]))
