Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if 2**n > n**2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    if 2**n > n**2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    if (2**n > n**2):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    n = int(input())
    if 2**n > n**2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
  n = int(input())
  if 2**n > n**2:
    print('Yes')
  else:
    print('No')

main()

=======
Suggestion 6

def check(n):
    if 2**n > n**2:
        print("Yes")
    else:
        print("No")

n = int(input())
check(n)

=======
Suggestion 7

def main():
    import sys
    n = int(sys.stdin.readline())
    if 2**n > n**2:
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 8

def power_of_two(n):
    if n == 1:
        return True
    if n % 2 == 0:
        return power_of_two(n/2)
    else:
        return False
