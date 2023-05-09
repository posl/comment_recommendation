Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n < 1000:
        print("ABC")
    else:
        print("ABD")

=======
Suggestion 2

def main():
    n = int(input())
    if n <= 999:
        print("ABC")
    else:
        print("ABD")

=======
Suggestion 3

def main():
    N = int(input())
    if N <= 999:
        print("ABC")
    else:
        print("ABD")

=======
Suggestion 4

def main():
    # input
    N = int(input())

    # compute

    # output
    if N < 1000:
        print('ABC')
    else:
        print('ABD')

=======
Suggestion 5

def main():
    n = int(input())
    print("ABC" if n < 1000 else "ABD")

=======
Suggestion 6

def main():
    # Take input Here and Call solution function
    n = int(input())
    #print(n)
    if n <= 999:
        print('ABC')
    else:
        print('ABD')

=======
Suggestion 7

def get_round_label(round_number):
    if round_number < 1000:
        return "ABC"
    else:
        return "ABD"
