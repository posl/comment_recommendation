def getGrade(n):
    if n >= 0 and n < 40:
        return 40 - n
    elif n >= 40 and n < 70:
        return 70 - n
    elif n >= 70 and n < 90:
        return 90 - n
    else:
        return "expert"

if __name__ == '__main__':
    getGrade()