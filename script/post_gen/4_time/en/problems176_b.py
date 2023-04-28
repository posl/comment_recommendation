Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

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
    while len(N) > 1:
        N = str(sum([int(i) for i in N]))
    if int(N) % 9 == 0:
        print('Yes')
    else:
        print('No')

main()

Code 2

=======
Suggestion 4

def main():
    N = input()
    if N == '0':
        print('Yes')
        return
    if int(N) % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    N = input()
    if N == "0":
        print("Yes")
        return
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N = input()
    while len(N) > 1:
        N = str(sum(map(int, N)))
    if N == '9':
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N = input()
    if N == '0':
        print('Yes')
    else:
        sum = 0
        for i in N:
            sum += int(i)
        if sum % 9 == 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    N = input()
    while len(N) > 1:
        N = str(sum(map(int, list(N))))
    print('Yes' if N == '9' else 'No')

main()

=======
Suggestion 9

def main():
    N = input()
    if N == '0':
        print('Yes')
        return
    if int(N[-1]) % 2 == 0:
        print('No')
        return
    ans = 0
    for i in range(len(N)):
        ans += int(N[i])
    if ans % 9 == 0:
        print('Yes')
    else:
        print('No')
