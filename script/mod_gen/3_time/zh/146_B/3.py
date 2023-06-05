def shift(s,n):
    result = ""
    for c in s:
        if ord(c) + n > ord('Z'):
            result += chr(ord(c) + n - ord('Z') + ord('A') - 1)
        else:
            result += chr(ord(c) + n)
    return result

if __name__ == '__main__':
    shift()