Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a * 1 <= b <= a * 6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def solve():
    a, b = map(int, input().split())
    if a * 1 <= b <= a * 6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a * 6 >= b and a <= b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a <= b <= 6 * a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if 6 * A >= B and A <= B:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if 6*a >= b >= a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if 1 <= a <= 100 and 1 <= b <= 1000:
        if a <= b <= 6*a:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a <= b <= a*6:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    if A * 6 >= B and A <= B:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def dice(a,b):
  for i in range(1,a+1):
    for j in range(1,a+1):
      if i+j == b:
        return 'Yes'
  return 'No'

a,b = map(int,input().split())
print(dice(a,b))
