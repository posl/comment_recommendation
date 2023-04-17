Synthesizing 10/10 solutions

=======

def main():
    a, b = map(int, input().split())
    if (a * b) % 2 == 0:
        print("No")
    else:
        print("Yes")

=======

def main():
    A, B = map(int, input().split())
    if (A * B) % 2 == 1:
        print("Yes")
    else:
        print("No")

=======

def main():
    a, b = map(int, input().split())
    if (a * b) % 2 == 0:
        print('No')
    else:
        print('Yes')

=======

def main():
    A, B = map(int, input().split())
    if A * B % 2 == 1:
        print("Yes")
    else:
        print("No")

=======

def main():
    A, B = [int(x) for x in input().split()]
    if (A * B) % 2 == 1:
        print("Yes")
    else:
        print("No")

=======

def main():
    a, b = map(int, input().split())
    if (a*b)%2 == 0:
        print("No")
    else:
        print("Yes")

main()

=======

def main():
    A, B = map(int, input().split())
    if A == 1 or B == 1:
        print('Yes')
    else:
        print('No')

=======

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print("No")
    else:
        print("Yes")

=======

def main():
    A, B = map(int, input().split())
    if A*B%2 == 1:
        print('Yes')
    else:
        print('No')

=======

def main():
    A, B = map(int, input().split())
    print('Yes' if A*B%2 else 'No')
