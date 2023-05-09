def get_permutations(string):
    if len(string) == 1:
        return [string]
    else:
        permutations = []
        for char in string:
            for permutation in get_permutations(string.replace(char, '', 1)):
                permutations.append(char + permutation)
        return permutations

if __name__ == '__main__':
    get_permutations()