def problem146_b():
    n = int(input())
    s = input()
    result = ''
    for i in range(len(s)):
        result += chr((ord(s[i]) - 65 + n) % 26 + 65)
    print(result)
