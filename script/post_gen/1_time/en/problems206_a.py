Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N * 1.08 < 206:
        print("Yay!")
    elif N * 1.08 == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 2

def main():
    N = int(input())
    if N * 1.08 < 206:
        print('Yay!')
    elif N * 1.08 == 206:
        print('so-so')
    else:
        print(':(')

=======
Suggestion 3

def main():
    N = int(input())
    if N * 108 < 20600:
        print("Yay!")
    elif N * 108 == 20600:
        print("so-so")
    else:
        print(":(")

main()

I am using Python 3.4.3 and I am getting the following error:

Traceback (most recent call last):
  File "problems206_a.py", line 31, in <module>
    main()
  File "problems206_a.py", line 29, in main
    print("so-so")
UnicodeEncodeError: 'ascii' codec can't encode character '\u2212' in position 0: ordinal not in range(128)

I am not sure how to fix this. I have tried to add the following line to the top of the file:

=======
Suggestion 4

def main():
    N = int(input())
    if N == 206:
        print("so-so")
    elif N < 206:
        print("Yay!")
    else:
        print(":(")

main()

=======
Suggestion 5

def main():
    N = int(input())
    tax = N * 1.08
    if tax > 206:
        print(':(')
    elif tax < 206:
        print('Yay!')
    else:
        print('so-so')

=======
Suggestion 6

def main():
    N = int(input())

    tax_included = int(N * 1.08)

    if tax_included < 206:
        print("Yay!")
    elif tax_included == 206:
        print("so-so")
    else:
        print(":(")

main()

You can also use the floor division operator (//) to get the same result as int().

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    ans = int(N * 1.08)
    if ans < 206:
        print("Yay!")
    elif ans == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 8

def solve():
    N = int(input())
    ans = N * 1.08
    if ans < 206:
        print("Yay!")
    elif ans == 206:
        print("so-so")
    else:
        print(":(")
solve()

=======
Suggestion 9

def main():
    # put your code here
    N = int(input())
    if N * 1.08 < 206:
        print("Yay!")
    elif N * 1.08 == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 10

def main():
    N = int(input())
    tax = 1.08
    price = int(tax * N)
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")
