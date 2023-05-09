def is_possible(s1, s2):
    if s1[0] == '#' and s1[1] == '#':
        return 'Yes'
    elif s2[0] == '#' and s2[1] == '#':
        return 'Yes'
    elif s1[0] == '#' and s2[0] == '#':
        return 'Yes'
    elif s1[1] == '#' and s2[1] == '#':
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    is_possible()