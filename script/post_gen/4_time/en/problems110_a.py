Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    print(A + B + C + max(A * 10 + B + C, A + B * 10 + C, A + B + C * 10))

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(max(a+b+c, a*b*c, (a+b)*c, a*(b+c)))

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A+B*C, A*B+C, A*B*C))

main()

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(max(a+b+c, a+b*c, a*(b+c), a*b*c))

=======
Suggestion 5

def main():
    # Read input
    A, B, C = map(int, input().split())
    # Calculate and print output
    print(max(A + B + C, A * B * C, (A + B) * C, A * (B + C)))

=======
Suggestion 6

def main():
    # read input
    a, b, c = map(int, input().split())

    # solve
    result = max(a+b+c, a+b*c, a*b+c, a*b*c, (a+b)*c, a*(b+c))

    # output
    print(result)

=======
Suggestion 7

def max_allowance(a,b,c):
    print(max(a+b+c, a*b*c, (a+b)*c, a*(b+c)))

=======
Suggestion 8

def main():
    # Get the input
    a,b,c = input().split()
    # Convert the string to integer
    a = int(a)
    b = int(b)
    c = int(c)
    # Create a list of all the possible numbers
    num_list = [a,b,c]
    # Sort the list
    num_list.sort()
    # Create a list of all the possible combinations
    comb_list = [(num_list[0],num_list[1]),(num_list[1],num_list[2]),(num_list[0],num_list[2])]
    # Create a list to hold the results
    result_list = []
    # Loop through the combinations
    for i in comb_list:
        # Add the results to the list
        result_list.append((i[0]*10)+i[1])
        result_list.append((i[0])+i[1])
    # Sort the results
    result_list.sort()
    # Print the last result
    print(result_list[-1])

=======
Suggestion 9

def max_allowance(A,B,C):
    # A,B,C are the values on the integer panels
    #return the maximum possible allowance
    return max(A+B+C, A*B*C, (A+B)*C, A*(B+C))

=======
Suggestion 10

def main():
    # Write code here
    print("Hello World!")
