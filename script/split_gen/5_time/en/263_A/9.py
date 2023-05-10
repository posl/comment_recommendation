def main():
    #input_string = input()
    #input_string = "1 2 1 2 1"
    input_string = "12 12 11 1 2"
    input_string = input_string.split()
    input_string = [int(i) for i in input_string]
    input_string.sort()
    #print(input_string)
    if (input_string[0] == input_string[1] and input_string[0] == input_string[2] and input_string[3] == input_string[4]):
        print("Yes")
    elif (input_string[0] == input_string[1] and input_string[2] == input_string[3] and input_string[2] == input_string[4]):
        print("Yes")
    else:
        print("No")
