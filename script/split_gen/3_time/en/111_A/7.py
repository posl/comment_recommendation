def main():
    # Read input
    n = input()
    # Replace 9 with 1 and 1 with 9
    n = n.replace('9', 'x')
    n = n.replace('1', '9')
    n = n.replace('x', '1')
    # Print output
    print(n)
