def solve():
    s = input()
    for i in range(len(s)):
        if i%2 == 0:
            if s[i] == "L":
                return "No"
        else:
            if s[i] == "R":
                return "No"
    return "Yes"
