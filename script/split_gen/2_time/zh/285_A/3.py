def solve(a, b):
    if a == 1:
        if b == 2 or b == 3 or b == 5 or b == 7 or b == 11 or b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 2:
        if b == 3 or b == 5 or b == 7 or b == 11 or b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 3:
        if b == 5 or b == 7 or b == 11 or b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 4:
        if b == 5 or b == 7 or b == 11 or b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 5:
        if b == 7 or b == 11 or b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 6:
        if b == 7 or b == 11 or b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 7:
        if b == 11 or b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 8:
        if b == 11 or b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 9:
        if b == 11 or b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 10:
        if b == 11 or b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 11:
        if b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 12:
        if b == 13:
            return "Yes"
        else:
            return "No"
    elif a == 13:
        return "No"
    else:
        return "No"
a, b = map(int, input().split())
print(solve(a, b))
