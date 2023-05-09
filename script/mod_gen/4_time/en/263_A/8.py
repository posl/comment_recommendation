def checkFullHouse():
    input = raw_input().split()
    input.sort()
    if (input[0] == input[1] and input[3] == input[4] and (input[2] == input[1] or input[2] == input[3])):
        print "Yes"
    else:
        print "No"
checkFullHouse()

if __name__ == '__main__':
    checkFullHouse()