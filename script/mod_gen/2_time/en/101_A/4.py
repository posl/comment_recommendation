def main():
    # Read input
    s = input()
    # Solve problem
    result = 0
    for i in range(4):
        if s[i] == '+':
            result += 1
        else:
            result -= 1
    # Output result
    print(result)

if __name__ == '__main__':
    main()