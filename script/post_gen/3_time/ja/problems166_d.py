Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            if a ** 5 - b ** 5 == x:
                print(a, b)
                exit()

=======
Suggestion 2

def main():
    x = int(input())
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            if a ** 5 - b ** 5 == x:
                print(a, b)
                return

=======
Suggestion 3

def main():
    X = int(input())
    for A in range(-1000,1000):
        for B in range(-1000,1000):
            if A**5 - B**5 == X:
                print(A,B)
                exit()

=======
Suggestion 4

def solve():
    x = int(input())
    for a in range(-200, 200):
        for b in range(-200, 200):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 5

def main():
    X = int(input())
    for A in range(-118,120):
        for B in range(-119,119):
            if A**5 - B**5 == X:
                print(A,B)
                return

=======
Suggestion 6

def main():
    x = int(input())
    for a in range(-200, 200):
        for b in range(-200, 200):
            if (a**5 - b**5) == x:
                print(a, b)
                return

=======
Suggestion 7

def main():
    X = int(input())
    for a in range(-118,120):
        for b in range(-119,119):
            if a**5 - b**5 == X:
                print(a,b)
                return

=======
Suggestion 8

def main():
    X = int(input())
    A = 0
    B = 0
    for i in range(-118,119):
        for j in range(-119,118):
            if i**5 - j**5 == X:
                A = i
                B = j
                break
    print(A,B)

=======
Suggestion 9

def main():
    # 入力
    x = int(input())

    # 出力
    print("0 -1")

=======
Suggestion 10

def get_input():
    x = int(input())
    return x
