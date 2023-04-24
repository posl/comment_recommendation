Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            count += 1
    print(count)

main()

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 != 0:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    N = int(input())
    if N < 10:
        print(N)
    else:
        print(9 + (N - 9) // 10)

main()

=======
Suggestion 6

def main():
    N = int(input())
    if N < 10:
        print(N)
    else:
        print(9 + (N-9)//10)

=======
Suggestion 7

def main():
    N = int(input())
    ans = N//10*9 + max(0, N%10 - 9 + 1)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    print(N//10*9 + (N%10+1)//2)

=======
Suggestion 9

def main():
    N = int(input())
    print(int(N/2) + int(N%2))

=======
Suggestion 10

def num_digits(n):
    return len(str(n))
