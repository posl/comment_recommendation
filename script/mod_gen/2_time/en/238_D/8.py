def isYes(a, s):
    if a == 0:
        if s == 0:
            return "Yes"
        else:
            return "No"
    if s < a:
        return "No"
    if s % 2 == 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    isYes()