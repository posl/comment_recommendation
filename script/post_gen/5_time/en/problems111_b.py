Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n <= 111:
        print(111)
    elif n <= 222:
        print(222)
    elif n <= 333:
        print(333)
    elif n <= 444:
        print(444)
    elif n <= 555:
        print(555)
    elif n <= 666:
        print(666)
    elif n <= 777:
        print(777)
    elif n <= 888:
        print(888)
    elif n <= 999:
        print(999)

=======
Suggestion 2

def main():
    n = int(input())
    if n < 111:
        print(111)
    elif 111 <= n < 222:
        print(111)
    elif 222 <= n < 333:
        print(222)
    elif 333 <= n < 444:
        print(333)
    elif 444 <= n < 555:
        print(444)
    elif 555 <= n < 666:
        print(555)
    elif 666 <= n < 777:
        print(666)
    elif 777 <= n < 888:
        print(777)
    elif 888 <= n < 999:
        print(888)
    else:
        print(999)

=======
Suggestion 3

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print(((N // 111) + 1) * 111)

=======
Suggestion 4

def main():
    N = int(input())

    if N % 111 == 0:
        print(N)
    else:
        print((N // 111 + 1) * 111)

=======
Suggestion 5

def main():
    n = int(input())
    while True:
        if len(set(list(str(n)))) == 1:
            print(n)
            break
        n += 1

=======
Suggestion 6

def main():
    n = int(input())
    while True:
        if len(set(str(n))) == 1:
            print(n)
            return
        else:
            n += 1

=======
Suggestion 7

def Main():
    n = input()
    if n[0] == n[1] == n[2]:
        print(n)
    else:
        print(n[0]*3)

=======
Suggestion 8

def main():
    N = int(input())
    print((N//111+1)*111)

=======
Suggestion 9

def main():
    # Get the input
    N = int(input())

    # Find the next ABC number
    while True:
        if N % 111 == 0:
            break
        N += 1

    # Print the output
    print(N)
