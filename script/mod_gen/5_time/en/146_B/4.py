def rotate(s, n):
    result = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                result += chr((ord(c) - 65 + n) % 26 + 65)
            else:
                result += chr((ord(c) - 97 + n) % 26 + 97)
        else:
            result += c
    return result

if __name__ == '__main__':
    rotate()