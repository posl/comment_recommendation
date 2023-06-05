Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    for i in range(10000):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    for i in range(1,101):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 3

def main():
    A,B=map(int,input().split())
    for i in range(1,1000):
        if int(i*0.08)==A and int(i*0.1)==B:
            print(i)
            break
    else:
        print(-1)

main()

=======
Suggestion 4

def main():
    a, b = map(int, input().split())

    for i in range(1, 101):
        if (int(i * 0.08) == a) and (int(i * 0.1) == b):
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 5

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

import math
a, b = map(int, input().split())
n = 1
while True:
    if round_up(n * 0.08) == a and round_up(n * 0.1) == b:
        print(n)
        break
    elif round_up(n * 0.08) > a or round_up(n * 0.1) > b:
        print(-1)
        break
    else:
        n += 1

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    for i in range(1, 101):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
    print(-1)

=======
Suggestion 7

def input_data():
    a,b = map(int, input().split())
    return a,b

=======
Suggestion 8

def get_price(a, b):
    for i in range(100):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            return i
    return -1

=======
Suggestion 9

def tax(a,b):
    for i in range(1,100):
        if int(i*0.08) == a and int(i*0.1) == b:
            return i
    return -1
