Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print(N + (111 - N % 111))

=======
Suggestion 2

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print((N // 111 + 1)*111)

=======
Suggestion 3

def main():
    N = int(input())
    print(((N - 1) // 111 + 1) * 111)

=======
Suggestion 4

def main():
    N = int(input())
    print((N + 111) // 111 * 111)

=======
Suggestion 5

def main():
    n = int(input())
    print((n + 111) // 111 * 111)

=======
Suggestion 6

def main():
    N = int(input())
    i = 1
    while True:
        if N < 111 * i:
            print(111 * i)
            return
        i += 1

=======
Suggestion 7

def main():
    N = int(input())
    print((N + 222) // 111 * 111)

=======
Suggestion 8

def main():
    #write your code here
    n = int(input())
    ans = (n + 111) // 111 * 111
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    print((N+111)//111*111)
main()
