def check(s1,s2):
    if s1[0][0] == '#' and s1[0][1] == '#' and s1[1][0] == '#' and s1[1][1] == '#':
        return 'Yes'
    elif s2[0][0] == '#' and s2[0][1] == '#' and s2[1][0] == '#' and s2[1][1] == '#':
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    check()