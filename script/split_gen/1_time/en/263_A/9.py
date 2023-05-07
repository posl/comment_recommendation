def main():
    # read input
    # split the input into a list of strings
    # convert the list of strings into a list of integers
    # assign each integer to a variable
    a,b,c,d,e = [int(x) for x in input().split()]
    # use a set to get a list of unique values
    # if the length of the set is 2, then there are 3 cards with one value and 2 cards with another value
    if len(set([a,b,c,d,e])) == 2:
        print("Yes")
    else:
        print("No")
main()
This code is a little different from the other solutions. It uses a set to get a list of unique values. If the length of the set is 2, then there are 3 cards with one value and 2 cards with another value.
The code is pretty simple. It reads the input and converts it to a list of integers. It then uses a set to get a list of unique values. If the length of the set is 2, then there are 3 cards with one value and 2 cards with another value. The code then prints Yes o
