def split_pin(s):
    for i in range(1, 10):
        if s[i] == "0":
            if s[i + 1] == "0":
                return "Yes"
            else:
                return "No"
    return "No"
s = input()
print(split_pin(s))
