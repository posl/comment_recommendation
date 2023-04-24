Synthesizing 10/10 solutions (Duplicates hidden)

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

main()

=======
Suggestion 2

def main():
    N = input()
    if int(N) % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = input()
    if int(N) % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n = input()
    if int(n) % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    if n % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N = input()
    while len(N) > 1:
        N = str(sum([int(x) for x in N]))
    if N == '9':
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 7

def main():
    N = input()
    if int(N) % 9 == 0:
        print("Yes")
    else:
        print("No")
    return

=======
Suggestion 8

def main():
    n = input()
    while len(n) > 1:
        n = str(sum(map(int, n)))
    print("Yes" if n == "9" else "No")

=======
Suggestion 9

def sum_digits(n):
    return sum(int(i) for i in str(n))
