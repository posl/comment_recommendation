def main():
    # Take input from stdin
    s = input()
    # Compute result
    result = 1
    for i in range(1, len(s) + 1):
        result *= i
    # Print result to stdout
    print(result)
