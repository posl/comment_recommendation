def problem122_b():
    s = input()
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "T" or s[i] == "G" or s[i] == "C":
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)
problem122_b()
