def get_numbers(s):
    return [ord(c)-ord('a') for c in s]

if __name__ == '__main__':
    get_numbers()