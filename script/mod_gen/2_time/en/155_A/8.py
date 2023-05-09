def isPoor(a, b, c):
    if a != b and a != c and b != c:
        return "No"
    elif a == b and b == c:
        return "No"
    else:
        return "Yes"

if __name__ == '__main__':
    isPoor()