Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(65, 65 + k)]))

=======
Suggestion 2

def main():
    k = int(input())
    print("".join([chr(i) for i in range(65, 65 + k)]))

=======
Suggestion 3

def main():
    k = int(input())
    print(''.join(chr(ord('A') + i) for i in range(k)))

=======
Suggestion 4

def main():
    k = int(input())
    print(''.join([chr(65+i) for i in range(k)]))

=======
Suggestion 5

def main():
    k = int(input())
    print(''.join(chr(i) for i in range(65, 65 + k)))

=======
Suggestion 6

def main():
    K = int(input())
    print(''.join(chr(i) for i in range(ord('A'), ord('A')+K)))

=======
Suggestion 7

def main():
    k = int(input())
    ans = ""
    for i in range(k):
        ans += chr(i+65)
    print(ans)

=======
Suggestion 8

def main():
    k = int(input())
    print("".join(map(chr, range(65, 65+k))))

=======
Suggestion 9

def main():
    k = int(input())

    print(''.join([chr(x) for x in range(65, 65 + k)]))

=======
Suggestion 10

def main():
    #read the number of letters
    k = int(input())
    #print the first k uppercase letters in ascending order
    print(''.join([chr(i) for i in range(65,65+k)]))
