Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = input()
    if N[0] == '7' or N[1] == '7' or N[2] == '7':
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N = input()
    if "7" in N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = int(input())
    if N % 10 == 7 or N // 10 % 10 == 7 or N // 100 == 7:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = input()
    if '7' in N:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    n = int(input())
    if n // 100 == 7 or n % 100 // 10 == 7 or n % 10 == 7:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N = int(input())
    if N//100 == 7 or N%100//10 == 7 or N%10 == 7:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = input()
    if N.count("7") > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n = input()
    if n.count("7") >= 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N = input()
    if N.count("7") == 0:
        print("No")
    else:
        print("Yes")
