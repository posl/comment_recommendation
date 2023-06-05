Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = int(input())
    print(a+a*a+a*a*a)

=======
Suggestion 2

def main():
    a = int(input())
    print(a + a**2 + a**3)

=======
Suggestion 3

def main():
    a = int(input())
    print(a+a**2+a**3)
    return 0

=======
Suggestion 4

def main():
    a = int(input())
    result = 0
    for i in range(1,4):
        result += a**i
    print(result)
main()
