Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print(int((a + b) / 2))
    else:
        print('IMPOSSIBLE')

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 4

def problems135_a():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 5

def main():
    A, B = [int(x) for x in input().split()]
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    k = (a+b)/2
    if k.is_integer():
        print(int(k))
    else:
        print('IMPOSSIBLE')

=======
Suggestion 7

def problems135_a(a,b):
    if (a+b)%2 == 0:
        return int((a+b)/2)
    else:
        return "IMPOSSIBLE"

=======
Suggestion 8

def main():
    #input
    A,B = map(int, input().split())
    #output
    if (A+B)%2 == 0:
        print(int((A+B)/2))
    else:
        print("IMPOSSIBLE")
