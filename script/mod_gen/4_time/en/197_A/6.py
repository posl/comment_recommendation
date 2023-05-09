def main():
    # Read input
    s = list(input())
    # Move the first character to the end
    s.append(s.pop(0))
    # Print result
    print(''.join(s))

if __name__ == '__main__':
    main()