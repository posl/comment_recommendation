Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if A**2 + B**2 < C**2:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a**2 + b**2 < c**2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a**2 + b**2 < c**2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    if (A ** 2 + B ** 2) < C ** 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b, c = [int(x) for x in input().split()]
    if a**2 + b**2 < c**2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    # 入力
    A, B, C = map(int, input().split())
    # 出力
    print("Yes" if A**2 + B**2 < C**2 else "No")

=======
Suggestion 7

def main():
    A,B,C = (int(x) for x in input().split())
    if (A**2 + B**2) < C**2:
        print('Yes')
    else:
        print('No')
