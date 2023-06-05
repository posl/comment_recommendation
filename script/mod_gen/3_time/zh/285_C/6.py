def get_index(s):
    count = 0
    for i in range(len(s)):
        count += (26 ** (i + 1))
    return count

if __name__ == '__main__':
    get_index()