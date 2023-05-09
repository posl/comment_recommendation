Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    a = int(s[0])
    b = int(s[2])
    print(a*b)

=======
Suggestion 2

def main():
    S = input()
    a = int(S[0])
    b = int(S[2])
    print(a*b)

=======
Suggestion 3

def main():
    # input
    S = input()

    # compute

    # output
    print(int(S[0])*int(S[2]))

=======
Suggestion 4

def main():
    s = input()
    a = s[0]
    b = s[2]
    print(int(a)*int(b))

=======
Suggestion 5

def main():
    S = input()
    a = int(S[0])
    b = int(S[2])
    print(a*b)

main()

=======
Suggestion 6

def main():
    s = input()
    a, b = s.split('x')
    print(int(a) * int(b))

=======
Suggestion 7

def main():
    # Take input from stdin
    S = input()
    # Split the string into a list of chars
    S_list = list(S)
    # Remove the x
    S_list.remove('x')
    # Convert the list of chars to a list of ints
    S_list = [int(i) for i in S_list]
    # Multiply the integers in the list
    product = S_list[0] * S_list[1]
    # Print the product
    print(product)

main()
