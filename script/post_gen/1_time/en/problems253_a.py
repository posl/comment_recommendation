Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a <= b and b <= c:
        print("Yes")
    elif c <= b and b <= a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def is_median(a, b, c):
    if b > a and b < c:
        return True
    elif b < a and b > c:
        return True
    else:
        return False

=======
Suggestion 5

def main():
    # Take input Here and Call solution function
    a,b,c = map(int,input().strip().split())
    print(solution(a,b,c))

=======
Suggestion 6

def main():
    #a, b, c = map(int, input().split())
    a, b, c = map(int, "2 5 3".split())
    if b <= a and b >= c or b >= a and b <= c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def check_median(a,b,c):
    if b in range(min(a,c),max(a,c)+1):
        return True
    else:
        return False
