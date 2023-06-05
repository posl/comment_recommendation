def moveN(string, n):
    result = ""
    for i in string:
        #print(ord(i))
        if (ord(i) + n) > 90:
            result += chr(ord(i) + n - 26)
        else:
            result += chr(ord(i) + n)
    return result

if __name__ == '__main__':
    moveN()