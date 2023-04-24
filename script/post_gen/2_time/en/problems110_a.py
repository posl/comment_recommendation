Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    print(max(A + B + C, 10 * A + B + C, A + 10 * B + C, A + B + 10 * C, 10 * A + 10 * B + C, 10 * A + B + 10 * C, A + 10 * B + 10 * C, 10 * A + 10 * B + 10 * C))

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(max(a + b * 10 + c, a * 10 + b + c, a + b + c * 10))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(a + b + c, a * b * c, a * b + c, a * (b + c), a + b * c, (a + b) * c))

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(max(A + B + C, A * B * C, A * (B + C), (A + B) * C))

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    print(max(a+b+c, a+b*c, (a+b)*c, a*b*c, a*b+c, a*(b+c)))

main()

=======
Suggestion 6

def main():
    A, B, C = input().split()
    A, B, C = int(A), int(B), int(C)
    print(max(A+B+C, A*B*C, A+B*C, A*B+C, (A+B)*C))

=======
Suggestion 7

def main():
    numbers = [int(x) for x in input().split()]
    numbers.sort()
    print((numbers[0] + numbers[1]) * 10 + numbers[2])

=======
Suggestion 8

def main():
    A,B,C = map(int, input().split())
    print(max(A+B+C, A+B*C, A*B+C, A*B*C))

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    print(max(a+b+c,a*b*c,a*(b+c),(a+b)*c))

=======
Suggestion 10

def main():
    # Read the input
    A, B, C = map(int, input().split())
    # Find the maximum possible amount of the allowance
    max_allowance = 0
    for i in range(1, 3):
        if i == 1:
            allowance = int(str(A) + str(B) + str(C))
        elif i == 2:
            allowance = int(str(A) + str(C) + str(B))
        if allowance > max_allowance:
            max_allowance = allowance
    print(max_allowance)
