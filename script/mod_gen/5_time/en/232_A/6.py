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
