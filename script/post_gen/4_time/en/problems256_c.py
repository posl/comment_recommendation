Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    return h1, h2, h3, w1, w2, w3

=======
Suggestion 2

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    if h1 + h2 + h3 == w1 + w2 + w3:
        print('1')
    else:
        print('0')

=======
Suggestion 3

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    if (h1 + h2 + h3) != (w1 + w2 + w3):
        print(0)
    else:
        print(1)

=======
Suggestion 4

def main():
    # h1, h2, h3, w1, w2, w3 = map(int, input().split())
    h1, h2, h3, w1, w2, w3 = 3, 4, 6, 3, 3, 7
    # h1, h2, h3, w1, w2, w3 = 3, 4, 5, 6, 7, 8
    # h1, h2, h3, w1, w2, w3 = 5, 13, 10, 6, 13, 9
    # h1, h2, h3, w1, w2, w3 = 20, 25, 30, 22, 29, 24
    if h1 == w1 and h2 == w2 and h3 == w3:
        print(1)
        exit(0)

    if h1 + h2 + h3 != w1 + w2 + w3:
        print(0)
        exit(0)

    if h1 == w1 and h2 == w2:
        print(1)
        exit(0)

    if h1 == w1 and h3 == w3:
        print(1)
        exit(0)

    if h2 == w2 and h3 == w3:
        print(1)
        exit(0)

    if h1 == w2 and h2 == w1:
        print(1)
        exit(0)

    if h1 == w3 and h3 == w1:
        print(1)
        exit(0)

    if h2 == w3 and h3 == w2:
        print(1)
        exit(0)

    print(0)

=======
Suggestion 5

def solve(h1, h2, h3, w1, w2, w3):
    if h1 + h2 + h3 != w1 + w2 + w3:
        return 0
    if h1 > w1 or h2 > w2 or h3 > w3:
        return 0
    if h1 + h2 > w1 + w2:
        return 0
    if h2 + h3 > w2 + w3:
        return 0
    if h3 + h1 > w3 + w1:
        return 0
    if h1 + h2 + h3 == w1 + w2 + w3:
        return 1

=======
Suggestion 6

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    if (h1+h2+h3) == (w1+w2+w3):
        print(1)
    else:
        print(0)

=======
Suggestion 7

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print((h1*w1)+(h2*w2)+(h3*w3)-(h1*h2)-(h1*h3)-(h2*h3))

=======
Suggestion 8

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print((h1*h2*h3*w1*w2*w3)//(h1*h2*w3+h2*h3*w1+h3*h1*w2))

=======
Suggestion 9

def main():
    # Get input here
    h1, h2, h3, w1, w2, w3 = map(int, input().strip().split())

    # Calculate result here
    result = 0
    result = h1*h2*h3*w1*w2*w3

    # Print output here
    print(result)

main()
