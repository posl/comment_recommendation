def main():
    #Read the input
    input = raw_input()
    #Split the input into a list of strings
    input = input.split()
    #Convert the list of strings into a list of integers
    input = [int(x) for x in input]
    #Create a set of the input
    input = set(input)
    #Print the length of the set
    print len(input)
