def main():
    # Read the input
    P = [int(x) for x in input().split()]
    # Create a list of 26 elements
    alphabet = [0]*26
    # For each element in P, add 1 to that element's index in alphabet
    for i in P:
        alphabet[i-1] += 1
    # Create a list of 26 elements
    output = [0]*26
    # For each element in alphabet, add the number of elements before that element to that element's index in output
    for i in range(len(alphabet)):
        output[i] = sum(alphabet[:i])
    # For each element in output, add 97 to that element's index in output
    for i in range(len(output)):
        output[i] += 97
    # Convert the list of ASCII values to a string
    output = ''.join(chr(i) for i in output)
    # Print the output
    print(output)
main()
My code is very similar to yours, except that I used the enumerate() function, which returns the index and the value for each element in a list. This made it easier to create the output list.
I think this is a good solution. If you want to make it more Pythonic, you can use a list comprehension for the output, and you can also use the chr() function to convert the ASCII values to letters.
Thank you for the reply! I didn't know about the enumerate() function. I'll look into it. I'm still learning Python so I'm trying to write as much code as I can to practice.
