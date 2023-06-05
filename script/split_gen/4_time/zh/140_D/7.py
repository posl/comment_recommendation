def calc_happy_people(s):
    happy_people = 0
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            happy_people += 1
    return happy_people
