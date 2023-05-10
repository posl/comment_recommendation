def swap(string, index1, index2):
    string = list(string)
    string[index1-1], string[index2-1] = string[index2-1], string[index1-1]
    return ''.join(string)

if __name__ == '__main__':
    swap()