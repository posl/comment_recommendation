def isMultipleOfEight(s):
    for i in range(1000, 10000):
        if len(set(str(i))) == 4 and i % 8 == 0:
            if set(str(i)).issubset(set(s)):
                return True
    return False

if __name__ == '__main__':
    isMultipleOfEight()