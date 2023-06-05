def get_index(s):
    index = 0
    for i in range(1, len(s)):
        index += 26 ** i
    for i in range(1, len(s)):
        index += 26 ** i * (ord(s[i]) - ord('A') - 1)
    index += ord(s[0]) - ord('A')
    return index + 1

if __name__ == '__main__':
    get_index()