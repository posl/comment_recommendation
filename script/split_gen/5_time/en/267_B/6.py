def is_split(s):
    # Pin 1 is knocked down.
    if s[0] != '0':
        return False
    # There are two different columns that satisfy both of the following conditions:
    # Each of the columns has one or more standing pins.
    # There exists a column between these columns such that all pins in the column are knocked down.
    standing_columns = []
    last_column = None
    for i in range(len(s)):
        if s[i] == '1':
            if last_column is None:
                last_column = i
            elif last_column + 1 != i:
                if len(standing_columns) == 2:
                    return False
                standing_columns.append((last_column, i))
                last_column = i
    if len(standing_columns) != 2:
        return False
    # There exists a column between these columns such that all pins in the column are knocked down.
    for i in range(standing_columns[0][1] + 1, standing_columns[1][0]):
        if s[i] == '1':
            return False
    return True
