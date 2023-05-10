Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def check(n):
    if n % 100 == 0 and n > 0:
        return True
    else:
        return False

=======
Suggestion 2

def main():
    x = int(input())
    if x >= 100 and x % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    x = int(input())
    if x % 100 == 0 and x != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def judge(X):
    if X%100 == 0 and X != 0:
        return "Yes"
    else:
        return "No"

X = int(input())
print(judge(X))

=======
Suggestion 5

def main():
    x = int(input())
    if x % 100 == 0 and x >= 100:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    x = int(input())
    print("Yes" if x % 100 == 0 and x >= 100 else "No")

=======
Suggestion 7

def run():
    x = int(input())
    if x >= 100 and x % 100 == 0:
        print('Yes')
    else:
        print('No')
