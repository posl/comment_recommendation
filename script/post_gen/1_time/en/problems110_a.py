Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(max(a + b + c, a * 10 + b + c, a + b * 10 + c, a + b + c * 10))

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, (A+B)*C, A*(B+C), A*B*C))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(a+b+c, a*b*c, a+b*c, a*b+c, (a+b)*c, a*(b+c)))

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(max(a+b+c, a+b*c, a*b+c, a*b*c))

main()

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(max(a+b+c, a+b*c, a*b+c, a*b*c))

=======
Suggestion 6

def main():
    a,b,c = [int(x) for x in input().split()]
    print(max(a+b+c, a+b*c, a*b+c, a*b*c, (a+b)*c, a*(b+c)))

=======
Suggestion 7

def max_allowance(a, b, c):
    return max(a + b + c, a * (b + c), (a + b) * c, a * b * c)

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    print(max(a+b+c,a*b*c,a*(b+c),(a+b)*c))

=======
Suggestion 9

def main():
    # Read the input
    A, B, C = map(int, input().split())
    # Print the result
    print(max(A+B+C, A+B*C, A*B+C, A*B*C))

=======
Suggestion 10

def main():
    input = raw_input()
    input = input.split()
    input = map(int, input)
    input.sort()
    print input[2]*10 + input[1] + input[0]
