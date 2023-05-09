def swap(string, a, b):
    string = list(string)
    string[a-1], string[b-1] = string[b-1], string[a-1]
    return ''.join(string)

if __name__ == '__main__':
    swap()