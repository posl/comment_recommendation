Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = input()
    sum = 0
    for i in range(len(N)):
        sum += int(N[i])
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N = input()
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = input()
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')
main()

=======
Suggestion 4

def main():
    N = input()
    if int(N) % 9 == 0:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 5

def main():
    N = input()
    if int(N) % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N = input()
    N = [int(i) for i in N]
    if sum(N)%9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = input()
    if N == "0":
        print("Yes")
        return
    if int(N[-1]) % 2 == 0:
        print("No")
        return
    if sum(map(int, N)) % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N = input()
    print('Yes' if sum(map(int, N)) % 9 == 0 else 'No')

=======
Suggestion 9

def main():
    N = input()
    N = N[::-1]
    N = [int(i) for i in N]
    N = sum(N)
    if N % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    N = input().strip()
    if sum(int(n) for n in N) % 9 == 0:
        print('Yes')
    else:
        print('No')
