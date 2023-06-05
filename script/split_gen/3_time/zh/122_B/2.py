def find_max_length_of_acgt(s):
    length = 0
    max_length = 0
    for i in s:
        if i == "A" or i == "C" or i == "G" or i == "T":
            length += 1
            if length > max_length:
                max_length = length
        else:
            length = 0
    return max_length
