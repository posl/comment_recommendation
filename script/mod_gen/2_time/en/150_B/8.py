def countABC(s):
    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == "ABC":
            count += 1
    return count

if __name__ == '__main__':
    countABC()