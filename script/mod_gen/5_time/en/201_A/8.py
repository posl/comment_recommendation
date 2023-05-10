def main():
    input = raw_input()
    input = input.split()
    input = map(int, input)
    input.sort()
    if input[2] - input[1] == input[1] - input[0]:
        print "Yes"
    else:
        print "No"

if __name__ == '__main__':
    main()