def check_grid(s1, s2):
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    check_grid()