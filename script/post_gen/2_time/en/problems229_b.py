Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a + b < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A + B < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a + b >= 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if (a + b) >= 10**10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if (A+B) >= 10**10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 6

def solve(a, b):
    if len(a) > len(b):
        return "Hard"
    elif len(a) < len(b):
        return "Easy"
    else:
        for i in range(len(a)):
            if a[i] > b[i]:
                return "Hard"
            elif a[i] < b[i]:
                return "Easy"
        return "Easy"

=======
Suggestion 7

def solve():
    a, b = map(int, input().split())
    if a + b >= 10 ** 18:
        print('Hard')
    else:
        print('Easy')

=======
Suggestion 8

def main():
	a, b = map(int, input().split())
	if a + b < 10**10:
		print("Easy")
	else:
		print("Hard")

=======
Suggestion 9

def main():
    # input
    a,b = map(int, input().split())
    # check
    if a+b < 10**10:
        print('Easy')
    else:
        print('Hard')

=======
Suggestion 10

def solve():
    A, B = [int(x) for x in input().split()]
    print('Hard' if str(A + B)[-1] == '0' else 'Easy')
