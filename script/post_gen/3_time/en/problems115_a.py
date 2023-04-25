Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    D = int(input())
    if D == 25:
        print("Christmas")
    elif D == 24:
        print("Christmas Eve")
    elif D == 23:
        print("Christmas Eve Eve")
    elif D == 22:
        print("Christmas Eve Eve Eve")
    else:
        print("Invalid Input")

=======
Suggestion 2

def main():
    d = int(input())
    if d == 25:
        print("Christmas")
    elif d == 24:
        print("Christmas Eve")
    elif d == 23:
        print("Christmas Eve Eve")
    elif d == 22:
        print("Christmas Eve Eve Eve")

main()

I’m learning Python and I’m trying to make a program that will convert a number into a word. For example, if the user inputs the number 2, the program should output “Two”. I have a list of numbers and another list of words, and I’m trying to make a program that will compare the input with the numbers list and output the corresponding word from the words list. However, I’m having a hard time figuring out how to make the program compare the input with the numbers list. I’ve tried using the “in” operator, but it didn’t work. Here’s the code:

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
words = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen","Twenty"]

input = int(input("Enter a number: "))

=======
Suggestion 3

def main():
    d = int(input())
    if d == 25:
        print("Christmas")
    elif d == 24:
        print("Christmas Eve")
    elif d == 23:
        print("Christmas Eve Eve")
    elif d == 22:
        print("Christmas Eve Eve Eve")

=======
Suggestion 4

def main():
    D = int(input())
    if D == 25:
        print('Christmas')
    elif D == 24:
        print('Christmas Eve')
    elif D == 23:
        print('Christmas Eve Eve')
    elif D == 22:
        print('Christmas Eve Eve Eve')

=======
Suggestion 5

def main():
    D = int(input())
    if D == 25:
        print("Christmas")
    elif D == 24:
        print("Christmas Eve")
    elif D == 23:
        print("Christmas Eve Eve")
    else:
        print("Christmas Eve Eve Eve")

=======
Suggestion 6

def main():
    d = int(input())
    if d == 25:
        print("Christmas")
    elif d == 24:
        print("Christmas Eve")
    elif d == 23:
        print("Christmas Eve Eve")
    else:
        print("Christmas Eve Eve Eve")

=======
Suggestion 7

def main():
    x = int(input())
    if x == 25:
        print("Christmas")
    elif x == 24:
        print("Christmas Eve")
    elif x == 23:
        print("Christmas Eve Eve")
    else:
        print("Christmas Eve Eve Eve")

main()

=======
Suggestion 8

def main():

    # Read the input
    D = int(input())

    # Write the output
    if D == 25:
        print("Christmas")
    elif D == 24:
        print("Christmas Eve")
    elif D == 23:
        print("Christmas Eve Eve")
    else:
        print("Christmas Eve Eve Eve")

=======
Suggestion 9

def main():
    d = int(input())
    print("Christmas" + " Eve" * (25 - d))
