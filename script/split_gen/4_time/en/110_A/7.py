def main():
    # Get the input
    a,b,c = input().split()
    # Convert the string to integer
    a = int(a)
    b = int(b)
    c = int(c)
    # Create a list of all the possible numbers
    num_list = [a,b,c]
    # Sort the list
    num_list.sort()
    # Create a list of all the possible combinations
    comb_list = [(num_list[0],num_list[1]),(num_list[1],num_list[2]),(num_list[0],num_list[2])]
    # Create a list to hold the results
    result_list = []
    # Loop through the combinations
    for i in comb_list:
        # Add the results to the list
        result_list.append((i[0]*10)+i[1])
        result_list.append((i[0])+i[1])
    # Sort the results
    result_list.sort()
    # Print the last result
    print(result_list[-1])
