def convert_to_int(string):
    return [ord(c) - ord('a') for c in string]

if __name__ == '__main__':
    convert_to_int()