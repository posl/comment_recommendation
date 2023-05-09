def main():
    # Read a line
    line = input()
    # Split the line into a list of strings
    line = line.split()
    # Convert the list of strings into a list of integers
    line = [int(x) for x in line]
    # Read another line
    line2 = input()
    # Split the line into a list of strings
    line2 = line2.split()
    # Convert the list of strings into a list of integers
    line2 = [int(x) for x in line2]
    # Sort the list
    line2.sort()
    # Add the first K elements of the list
    print(sum(line2[:line[1]]))
