def problems279_a():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "w":
            count += 1
    print(count * 2)
