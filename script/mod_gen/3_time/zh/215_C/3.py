def permutation(string, start, end):
    if start == end:
        print(''.join(string))
        return
    for i in range(start, end):
        string[start], string[i] = string[i], string[start]
        permutation(string, start+1, end)
        string[start], string[i] = string[i], string[start]

if __name__ == '__main__':
    permutation()