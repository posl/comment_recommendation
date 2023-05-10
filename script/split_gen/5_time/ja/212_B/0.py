def weak_or_strong(num):
    if num[0] == num[1] and num[1] == num[2] and num[2] == num[3]:
        return "Weak"
    elif num[0] == "9" and num[1] == "8" and num[2] == "7" and num[3] == "6":
        return "Weak"
    elif int(num[0]) == int(num[1]) - 1 and int(num[1]) == int(num[2]) - 1 and int(num[2]) == int(num[3]) - 1:
        return "Weak"
    else:
        return "Strong"
