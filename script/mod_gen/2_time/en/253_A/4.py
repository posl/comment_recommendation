def median(a,b,c):
    if b < a < c or c < a < b:
        return "Yes"
    elif a < b < c or c < b < a:
        return "Yes"
    elif a < c < b or b < c < a:
        return "Yes"
    elif b == a == c:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    median()