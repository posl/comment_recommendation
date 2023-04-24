Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(65, 65 + K)]))

main()

=======
Suggestion 2

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(65, 65+k)]))

=======
Suggestion 3

def main():
    K = int(input())
    print("".join([chr(i) for i in range(65, 65+K)]))

=======
Suggestion 4

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(65,65+K)]))

=======
Suggestion 5

def main():
    k = int(input())
    ans = ""
    for i in range(k):
        ans += chr(ord('A') + i)
    print(ans)

=======
Suggestion 6

def main():
    k = int(input())
    print(''.join(chr(i) for i in range(65,65+k)))

=======
Suggestion 7

def main():
    # get K
    k = int(input())
    
    # print out the answer
    print(''.join([chr(i) for i in range(65, 65 + k)]))

main()
