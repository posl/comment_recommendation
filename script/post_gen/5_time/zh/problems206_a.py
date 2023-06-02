Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N * 1.08 < 206:
        print('Yay!')
    elif N * 1.08 > 206:
        print(':(')
    else:
        print('so-so')

=======
Suggestion 2

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
Suggestion 3

def main():
    # input
    n = int(input())
    # process
    price = int(n * 1.08)
    # output
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 4

def main():
    # input
    n = int(input())

    # process
    n = int(n * 1.08)
    if n < 206:
        print('Yay!')
    elif n == 206:
        print('so-so')
    else:
        print(':(')

=======
Suggestion 5

def main():
    n = int(input())
    if int(n*1.08)<206:
        print("Yay!")
    elif int(n*1.08)==206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 6

def main():
    # input
    n = int(input())
    # process
    ans = 'Yay!' if int(1.08*n) < 206 else 'so-so' if int(1.08*n) == 206 else ':('
    # output
    print(ans)

=======
Suggestion 7

def main():
    input = int(input())
    price = int(input * 1.08)

    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 8

def main():
    #input
    N = int(input())
    #process
    #output
    if N*1.08<206:
        print("Yay!")
    elif N*1.08>206:
        print(":(")
    else:
        print("so-so")

=======
Suggestion 9

def main():
    N = int(input())
    print('Yay!' if int(N * 1.08) < 206 else 'so-so' if int(N * 1.08) == 206 else ':(')
