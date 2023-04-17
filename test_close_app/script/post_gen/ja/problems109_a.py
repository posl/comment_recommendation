Synthesizing 10/10 solutions (Duplicates hidden)

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
    if (A * B) % 2 == 0:
        print("No")
    else:
        print("Yes")

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
    ans = "No"
    for C in range(1, 4):
        if (A * B * C) % 2 == 1:
            ans = "Yes"
    print(ans)

=======

def main():
    a, b = map(int, input().split())
    if a * b % 2 == 1:
        print("Yes")
    else:
        print("No")

=======

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 1:
        print("No")
    else:
        print("Yes")

=======

def main():
    # A, B = map(int, input().split())
    A, B = map(int, input().split())
    if A % 2 == 1 and B % 2 == 1:
        print("Yes")
    else:
        print("No")

=======

def main():
    A,B = map(int, input().split())
    if A*B%2 == 1:
        print("Yes")
    else:
        print("No")

=======

def main():
    a,b = map(int, input().split())
    c = 1
    while c <= 3:
        if (a*b*c)%2 == 1:
            print("Yes")
            return
        c += 1
    print("No")
