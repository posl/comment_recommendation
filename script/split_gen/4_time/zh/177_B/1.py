def problem177_b():
    s = input()
    t = input()
    max = len(s)
    for i in range(len(s)):
        if len(s[i:i+len(t)]) < len(t):
            break
        count = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
        if count < max:
            max = count
    print(max)
