def isHardRead(s):
    odd = s[0::2]
    even = s[1::2]
    if odd.islower() and even.isupper():
        return "Yes"
    else:
        return "No"
