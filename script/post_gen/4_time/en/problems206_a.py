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
    tax = int(N * 1.08)
    if tax < 206:
        print("Yay!")
    elif tax == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 3

def main():
    N = int(input())
    price = int(N*1.08)
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 4

def main():
    N = int(input())
    if N*1.08 < 206:
        print("Yay!")
    elif N*1.08 > 206:
        print(":(")
    else:
        print("so-so")

=======
Suggestion 5

def main():
    N = int(input())
    if N < 206:
        print('Yay!')
    elif N == 206:
        print('so-so')
    else:
        print(':(')

=======
Suggestion 6

def main():
    N = int(input())
    if (N*1.08)//1 < 206:
        print('Yay!')
    elif (N*1.08)//1 > 206:
        print(':(')
    else:
        print('so-so')

=======
Suggestion 7

def main():
    N = int(input())
    tax = 1.08
    price = N * tax
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 8

def main():
    N = int(input())
    print("Yay!" if N*108//100 < 206 else ":(" if N*108//100 > 206 else "so-so")

=======
Suggestion 9

def main():
    n = int(input())
    #print(n)
    tax = int(n * 1.08)
    #print(tax)
    if tax < 206:
        print("Yay!")
    elif tax == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 10

def main():
    #input
    N = int(input())

    #calculate
    tax = 1.08
    price = int(N * tax)

    #output
    if price < 206:
        print('Yay!')
    elif price == 206:
        print('so-so')
    else:
        print(':(')
