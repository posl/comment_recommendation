def problems146_b():
    n = int(input())
    s = input()
    result = ""
    for i in range(len(s)):
        if s[i] != " ":
            if ord(s[i]) + n > 90:
                result += chr(ord(s[i]) + n - 26)
            else:
                result += chr(ord(s[i]) + n)
        else:
            result += " "
    print(result)
problems146_b()
