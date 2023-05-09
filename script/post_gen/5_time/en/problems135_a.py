Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print(int((a + b) / 2))
    else:
        print("IMPOSSIBLE")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 3

def problems135_a():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print(int((A + B) / 2))
    else:
        print("IMPOSSIBLE")

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if (a+b)%2 == 0:
        print((a+b)//2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    if (a+b)%2 == 0:
        print(int((a+b)/2))
    else:
        print('IMPOSSIBLE')

=======
Suggestion 6

def main():
    A, B = map(int, input().split())

    if (A+B)%2 == 0:
        print(int((A+B)/2))
    else:
        print('IMPOSSIBLE')

=======
Suggestion 7

def main():
    # input
    A,B = map(int,input().split())
    # compute
    if (A+B)%2 == 0:
        K = (A+B)//2
    else:
        K = "IMPOSSIBLE"
    # output
    print(K)

=======
Suggestion 8

def main():
    a,b = map(int, input().split())
    k = (a + b) // 2
    print(k if (a - k) == (k - b) else 'IMPOSSIBLE')

=======
Suggestion 9

def solve(a,b):
    if (a+b) % 2 == 0:
        return (a+b)//2
    else:
        return "IMPOSSIBLE"
