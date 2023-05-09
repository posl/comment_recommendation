def countABC(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'A':
            if i+2 < len(s):
                if s[i+1] == 'B':
                    if s[i+2] == 'C':
                        count += 1
    return count

if __name__ == '__main__':
    countABC()