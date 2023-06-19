Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x,y = map(int,input().split())
    if x < y:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x,y = map(int, input().split())
    if x<y:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x < y and x + 3 > y:
        print("Yes")
    elif x > y and x < y + 3:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    print('Yes' if x - y < 3 else 'No')

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x > y:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    if x < y:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 7

def main():
    x, y = map(int, input().split())
    print("Yes" if x < y and x + 3 > y else "No")
