Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    a, b, c = map(int, input().split())
    if (a == 5 and b == 5 and c == 7) or (a == 5 and b == 7 and c == 5) or (a == 7 and b == 5 and c == 5):
        print("YES")
    else:
        print("NO")

=======

def main():
    a, b, c = map(int, input().split())
    if (a == 5 and b == 7 and c == 5) or (a == 5 and b == 5 and c == 7) or (a == 7 and b == 5 and c == 5):
        print("YES")
    else:
        print("NO")

=======

def main():
    a, b, c = map(int, input().split())
    if a == 5 and b == 5 and c == 7:
        print("YES")
    elif a == 5 and b == 7 and c == 5:
        print("YES")
    elif a == 7 and b == 5 and c == 5:
        print("YES")
    else:
        print("NO")

=======

def main():
    a, b, c = map(int, input().split())
    if a == 5 and b == 5 and c == 7:
        print('YES')
    elif a == 5 and b == 7 and c == 5:
        print('YES')
    elif a == 7 and b == 5 and c == 5:
        print('YES')
    else:
        print('NO')

=======

def main():
    A, B, C = map(int, input().split())
    if A == 5 and B == 5 and C == 7:
        print('YES')
    elif A == 5 and B == 7 and C == 5:
        print('YES')
    elif A == 7 and B == 5 and C == 5:
        print('YES')
    else:
        print('NO')

=======

def main():
    A, B, C = map(int, input().split())
    if A == 5:
        if B == 7:
            if C == 5:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
