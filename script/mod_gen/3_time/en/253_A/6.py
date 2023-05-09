def isMedian(a, b, c):
    if (a < b and b < c) or (c < b and b < a):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    isMedian()