def getAnagramCount(s):
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count

if __name__ == '__main__':
    getAnagramCount()