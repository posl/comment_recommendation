Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if int(n*1.08) < 206:
        print("Yay!")
    elif int(n*1.08) == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 2

def main():
    N = int(input())
    if int(N * 1.08) < 206:
        print("Yay!")
    elif int(N * 1.08) == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 3

def main():
    n = int(input())
    if n * 1.08 < 206:
        print("Yay!")
    elif n * 1.08 == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 4

def main():
    n = int(input())
    print("Yay!" if int(n*1.08) < 206 else ":(" if int(n*1.08) > 206 else "so-so")

=======
Suggestion 5

def Main():
    N = int(input())
    if N*1.08 < 206:
        print("Yay!")
    elif N*1.08 > 206:
        print(":(")
    else:
        print("so-so")

=======
Suggestion 6

def problem206_a():
    N = int(input())
    price = int(1.08*N)
    if price < 206:
        print('Yay!')
    elif price == 206:
        print('so-so')
    else:
        print(':(')

=======
Suggestion 7

def main():
    n = int(input())
    price = 206
    tax = 1.08
    if n < price/tax:
        print("Yay!")
    elif n == price/tax:
        print("so-so")
    else:
        print(":(")
