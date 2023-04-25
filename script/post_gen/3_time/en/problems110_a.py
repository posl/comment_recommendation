Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A+B*C, A*B+C, A*B*C, (A+B)*C, A*(B+C)))

=======
Suggestion 2

def main():
    # Write your code here
    a, b, c = map(int, input().split())
    print(max(a*100+b*10+c, a*10+b+c*10, a*10+b+c, a+b*10+c*10, a+b*100+c*1, a+b*10+c*1))

main()

=======
Suggestion 3

def getAllowance(a, b, c):
    result = 0
    if a < b:
        temp = a
        a = b
        b = temp
    if a < c:
        temp = a
        a = c
        c = temp
    if b < c:
        temp = b
        b = c
        c = temp
    result = a * 10 + b + c
    return result

a, b, c = map(int, input().split())
print(getAllowance(a, b, c))

=======
Suggestion 4

def main():
    num = input().split()
    num.sort(reverse=True)
    print(num[0] + num[1] + num[2])

=======
Suggestion 5

def allowance(a,b,c):
    return max(a+b+c,a*b*c,(a+b)*c,a*(b+c))

a,b,c = map(int,input().split())
print(allowance(a,b,c))

Python 3.6.2

=======
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    print(max(9*10**2 + a+b+c, a*10**2 + b*10 + c + b*10 + c))

=======
Suggestion 7

def main():
    # Read the input
    A,B,C = map(int, input().split())
    
    # Find the maximum possible allowance
    maxAllowance = max(A+B+C, A+B*C, (A+B)*C, A*B*C, A*B+C, A*B+C)
    
    # Print the maximum possible allowance
    print(maxAllowance)

=======
Suggestion 8

def main():
    num = input().split()
    num.sort()
    print(num[2]+num[1]+num[0])

=======
Suggestion 9

def main():
    # read in the input
    a, b, c = map(int, input().split())
    # find the maximum possible amount of the allowance
    max_allowance = max(a+b+c, a*b*c, a*(b+c), (a+b)*c)
    # print the maximum possible amount of the allowance
    print(max_allowance)

=======
Suggestion 10

def main():
    # Read input
    input = raw_input()
    # Split input into a list
    input = input.split()
    # Convert the list into integers
    input = map(int, input)
    # Sort the list
    input.sort()
    # Convert the list into a string
    input = map(str, input)
    # Add the + sign to the middle of the list
    input.insert(1, '+')
    # Convert the list into a string
    input = ''.join(input)
    # Print the result
    print input
