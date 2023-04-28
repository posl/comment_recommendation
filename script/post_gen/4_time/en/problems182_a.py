Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(2 * a + 100 - b)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(2*A+100-B)

=======
Suggestion 3

def main():
    # Take input Here and Call solution function
    A, B = [int(x) for x in input().split(" ")]
    if B >= 2*A+100:
        print(0)
    else:
        print(2*A+100-B)
