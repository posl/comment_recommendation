def is_split(s):
    if s[0] == '0':
        return 'No'
    else:
        for i in range(1, 10):
            for j in range(i+1, 10):
                if s[i] == '1' and s[j] == '1':
                    for k in range(i+1, j):
                        if s[k] == '0':
                            return 'Yes'
        return 'No'

if __name__ == '__main__':
    is_split()