def main():
    input = raw_input()
    input = input.split()
    for i in range(26):
        input[i] = int(input[i])
    result = ''
    for i in range(26):
        result += chr(input[i]+96)
    print result

if __name__ == '__main__':
    main()