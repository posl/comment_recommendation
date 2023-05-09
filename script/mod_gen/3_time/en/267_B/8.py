def is_split(S):
    # Check for split
    # S is a string of length 10 consisting of 0 and 1.
    # If the placement of the pins represented by S is a split, return True; otherwise, return False.
    # Pin 1 is knocked down.
    # There are two different columns that satisfy both of the following conditions:
    # Each of the columns has one or more standing pins.
    # There exists a column between these columns such that all pins in the column are knocked down.
    if S[0] == "0":
        return False
    column1 = S[1:4]
    column2 = S[4:8]
    column3 = S[7:10]
    if column1.count("1") > 0 and column2.count("1") > 0 and column3.count("1") == 0:
        return True
    if column1.count("1") > 0 and column2.count("1") == 0 and column3.count("1") > 0:
        return True
    if column1.count("1") == 0 and column2.count("1") > 0 and column3.count("1") > 0:
        return True
    return False
S = input()

if __name__ == '__main__':
    is_split()