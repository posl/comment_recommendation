def poor(a,b,c):
    if a == b and b != c:
        return "Yes"
    elif a == c and b != c:
        return "Yes"
    elif b == c and a != c:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    poor()