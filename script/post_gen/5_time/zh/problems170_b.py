Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    X,Y = map(int,input().split())
    for i in range(X+1):
        j = X-i
        if 2*i + 4*j == Y:
            print("Yes")
            return
    print("No")
solve()

=======
Suggestion 2

def judge(x, y):
    for i in range(x+1):
        if 2*i + 4*(x-i) == y:
            return True
    return False

x, y = map(int, input().split())
print("Yes" if judge(x, y) else "No")

=======
Suggestion 3

def main():
    X,Y = map(int,input().split())
    for i in range(X+1):
        if 2*i + 4*(X-i) == Y:
            print("Yes")
            break
    else:
        print("No")

=======
Suggestion 4

def solve():
    x, y = map(int, input().split())
    for i in range(x+1):
        if i*2 + (x-i)*4 == y:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 5

def main():
    X,Y = map(int,input().split())
    if Y%2 == 0:
        if Y/2 <= X <= Y/4:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 6

def main():
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if Y % 2 == 0 and Y >= 2 * X and Y <= 4 * X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve():
    x, y = map(int, input().split())
    for i in range(x+1):
        if (2*i + 4*(x-i)) == y:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    x,y = map(int,input().split())
    if y%2 == 0 and y >= 2*x and y <= 4*x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def check(x,y):
    for i in range(x+1):
        if 2*i+4*(x-i)==y:
            return True
    return False

x,y=map(int,input().split())

=======
Suggestion 10

def anima_legs_check(num_anima, num_legs):
    for num_tur in range(num_anima + 1):
        num_crane = num_anima - num_tur
        if 2 * num_crane + 4 * num_tur == num_legs:
            return True

    return False
