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
    n = input()
    if "7" in n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    # input
    N = input()
    # compute
    if '7' in N:
        ans = 'Yes'
    else:
        ans = 'No'
    # output
    print(ans)

=======
Suggestion 4

def main():
    n = input()
    print("Yes" if "7" in n else "No")

=======
Suggestion 5

def check():
    N = input()
    if "7" in N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N = input()
    if '7' in N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = input()
    if "7" in N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def is_contain_7(num):
    while num > 0:
        if num % 10 == 7:
            return True
        num //= 10
    return False

N = int(input())
