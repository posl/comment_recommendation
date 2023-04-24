Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if int(n * 1.08) < 206:
        print("Yay!")
    elif int(n * 1.08) == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 2

def main():
    N = int(input())
    if int(N*1.08) < 206:
        print("Yay!")
    elif int(N*1.08) == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 3

def main():
    N = int(input())
    if int(N * 1.08) < 206:
        print('Yay!')
    elif int(N * 1.08) == 206:
        print('so-so')
    else:
        print(':(')

=======
Suggestion 4

def main():
    N = int(input())
    price = int(N * 1.08)
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 5

def main():
    n = int(input())
    price = int(n * 1.08)
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 6

def main():
    n = int(input())
    if int(1.08 * n) < 206:
        print("Yay!")
    elif int(1.08 * n) == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 7

def main():
    N = int(input())
    N = int(1.08 * N)
    if N < 206:
        print("Yay!")
    elif N == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 8

def main():
    N = int(input())
    if int(1.08 * N) < 206:
        print("Yay!")
    elif int(1.08 * N) > 206:
        print(":(")
    else:
        print("so-so")

=======
Suggestion 9

def main():
    # input
    N = int(input())

    # compute

    # output
    if int(N*1.08) < 206:
        print('Yay!')
    elif int(N*1.08) == 206:
        print('so-so')
    else:
        print(':(')

=======
Suggestion 10

def main():
    N = int(input())
    print("Yay!" if int(N * 1.08) < 206 else ":(" if int(N * 1.08) > 206 else "so-so")
