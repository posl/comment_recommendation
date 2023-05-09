def main():
    # get the input
    input_string = input()
    # split the input string into a list
    input_list = input_string.split()
    # create an empty list
    output_list = []
    # loop through the input list
    for i in input_list:
        # convert each item in the input list to an integer
        i = int(i)
        # append the integer to the output list
        output_list.append(i)
    # create an empty list
    alphabet_list = []
    # loop through the alphabet
    for i in range(97, 123):
        # convert each letter to a string
        i = chr(i)
        # append the string to the alphabet list
        alphabet_list.append(i)
    # create an empty list
    final_list = []
    # loop through the output list
    for i in output_list:
        # subtract one from each item in the output list
        i = i - 1
        # append the item to the final list
        final_list.append(i)
    # create an empty list
    final_list2 = []
    # loop through the final list
    for i in final_list:
        # append the item in the alphabet list at the index of the item in the final list
        final_list2.append(alphabet_list[i])
    # join the list into a string
    final_string = ''.join(final_list2)
    # print the final string
    print(final_string)

if __name__ == '__main__':
    main()