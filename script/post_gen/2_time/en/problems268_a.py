Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c, d, e = map(int, input().split())
    print(len(set([a, b, c, d, e])))

=======
Suggestion 2

def main():
    #input
    A, B, C, D, E = map(int, input().split())
    #output
    print(len(set([A, B, C, D, E])))

=======
Suggestion 3

def main():
    A,B,C,D,E = map(int, input().split())
    print(len(set([A,B,C,D,E])))

=======
Suggestion 4

def main():
    input_list = list(map(int, input().split()))
    print(len(set(input_list)))

=======
Suggestion 5

def main():
    A = list(map(int, input().split()))
    print(len(set(A)))

=======
Suggestion 6

def main():
    nums = map(int, raw_input().split())
    print len(set(nums))

=======
Suggestion 7

def main():
    s = set(map(int, input().split()))
    print(len(s))

=======
Suggestion 8

def main():
    print(len(set(input().split())))

=======
Suggestion 9

def main():
    #Read the input
    input = raw_input()
    #Split the input into a list of strings
    input = input.split()
    #Convert the list of strings into a list of integers
    input = [int(x) for x in input]
    #Create a set of the input
    input = set(input)
    #Print the length of the set
    print len(input)

=======
Suggestion 10

def main():
    # Get the input
    input = raw_input()
    # Split the input into a list
    input_list = input.split()
    # Convert the list of strings to a list of integers
    input_list = map(int, input_list)
    # Get the distinct integers in the list
    distinct_integers = set(input_list)
    # Print the number of distinct integers
    print len(distinct_integers)
