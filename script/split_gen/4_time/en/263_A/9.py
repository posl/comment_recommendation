def checkFullHouse(input):
    input = input.split()
    input.sort()
    if ((input[0] == input[1]) and (input[1] != input[2]) and (input[2] == input[3]) and (input[3] == input[4])):
        print("Yes")
    elif ((input[0] == input[1]) and (input[1] == input[2]) and (input[2] != input[3]) and (input[3] == input[4])):
        print("Yes")
    else:
        print("No")
input = input()
checkFullHouse(input)
