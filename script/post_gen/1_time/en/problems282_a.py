Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(65, 65+k)]))

main()

=======
Suggestion 2

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(65, 65+K)]))

=======
Suggestion 3

def main():
    k = int(input())
    print("".join([chr(i) for i in range(65, 65 + k)]))

=======
Suggestion 4

def main():
    k = int(input())
    print(''.join(chr(i) for i in range(ord('A'), ord('A') + k)))

=======
Suggestion 5

def main():
    k = int(input())
    print(''.join(chr(ord('A') + i) for i in range(k)))

=======
Suggestion 6

def main():
    k = int(input())
    print("".join([chr(c) for c in range(65, 65 + k)]))

main()

=======
Suggestion 7

def main():
    K = int(input())
    print("".join(chr(65+i) for i in range(K)))

=======
Suggestion 8

def main():
    # Put your code here
    input = int(input())
    print(''.join([chr(i) for i in range(65, 65+input)]))

main()

I was able to solve it with the following code:
