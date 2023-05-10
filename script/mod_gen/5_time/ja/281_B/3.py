def isUpperAlphabet(char):
    if ord(char) >= 65 and ord(char) <= 90:
        return True
    return False

if __name__ == '__main__':
    isUpperAlphabet()