Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n < 206:
        print("Yay!")
    elif n == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 2

def main():
    n = int(input())
    print("Yay!") if int(n*1.08) < 206 else print(":(") if int(n*1.08) > 206 else print("so-so")

=======
Suggestion 3

def main():
    n = int(input())
    if int(n*1.08) < 206:
        print("Yay!")
    elif int(n*1.08) == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 4

def main():
    N = int(input())
    price = int(1.08*N)
    if price < 206:
        print('Yay!')
    elif price == 206:
        print('so-so')
    else:
        print(':(')

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

def f(x):
    return int(1.08 * x)

N = int(input())

=======
Suggestion 7

def main():
    n = int(input())
    ans = int(n * 1.08)
    if ans < 206:
        print("Yay!")
    elif ans == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 8

def main():
    N = int(input())
    if N < 206:
        print("Yay!")
    elif N == 206:
        print("so-so")
    else:
        print(":(")
