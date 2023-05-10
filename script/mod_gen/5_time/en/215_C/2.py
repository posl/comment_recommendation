def permutations(string):
    if len(string) == 1:
        return [string]
    else:
        perms = []
        for char in string:
            for perm in permutations(string.replace(char, '', 1)):
                perms.append(char + perm)
        return perms

if __name__ == '__main__':
    permutations()