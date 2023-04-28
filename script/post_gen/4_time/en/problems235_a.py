Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a+b+c)

=======
Suggestion 2

def main():
    abc = input()
    abc = int(abc)
    a = int(abc / 100)
    b = int(abc / 10) - a * 10
    c = abc - a * 100 - b * 10
    print(a + b + c)

=======
Suggestion 3

def main():
    num = input()
    num = int(num)
    a = num // 100
    b = (num % 100) // 10
    c = num % 10
    print(a + b + c)

=======
Suggestion 4

def main():
    x = input()
    print(int(x[0]) + int(x[1]) + int(x[2]))

=======
Suggestion 5

def main():
    abc = int(input())
    bca = int(input())
    cab = int(input())
    print(abc + bca + cab)

=======
Suggestion 6

def main():
    # Take input here
    abc = input()

    # Compute the result here
    result = int(abc[0]) + int(abc[1]) + int(abc[2])

    # Print result here
    print(result)

=======
Suggestion 7

def main():
    input = raw_input()
    print int(input[0]) + int(input[1]) + int(input[2])
