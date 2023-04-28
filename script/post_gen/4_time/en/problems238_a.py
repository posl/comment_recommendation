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
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 3

def main():
    n = int(input())
    if 2**n > n**2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n = int(input())
    print("Yes" if 2**n > n**2 else "No")

=======
Suggestion 5

def main():
    n = int(input())
    # 2^n > n^2
    # 2^n > n * n
    # 2^n > n * n
    # 2^n - n * n > 0
    # 2^n - n^2 > 0
    if 2**n > n**2:
        print('Yes')
    else:
        print('No')
