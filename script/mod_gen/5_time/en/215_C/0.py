def permutations(string, step = 0):
    if step == len(string):
        # we've gotten to the end, print the permutation
        print("".join(string))
    for i in range(step, len(string)):
        # copy the string (store as array)
        string_copy = [character for character in string]
        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        # recurse on the portion of the stringthat has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)
