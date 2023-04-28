Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print(100 * (A - B) / A)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print((A-B)/A*100)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(100 * (1 - b/a))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print((1 - B/A) * 100)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    answer = 100 - (B / A) * 100
    print(answer)

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    print((a-b)/a*100)

=======
Suggestion 7

def main():
    a,b = map(int, input().split())
    print((1 - b/a)*100)

=======
Suggestion 8

def main():
    # A = regular price
    # B = discounted price
    A, B = [int(x) for x in input().split()]
    print(100 * (1 - B/A))

main()

=======
Suggestion 9

def main():
    A = int(input("A: "))
    B = int(input("B: "))
    print((A-B)/A*100)
