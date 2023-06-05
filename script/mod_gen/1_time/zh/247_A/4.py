def problem247_a():
    s = input()
    result = ""
    for i in range(len(s)):
        if i == len(s) - 1:
            result += "0"
        else:
            result += s[i + 1]
    print(result)
problem247_a()
