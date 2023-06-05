def problem146_b():
    n = int(input())
    s = input()
    result = ''
    for i in range(len(s)):
        result += chr((ord(s[i]) - 65 + n) % 26 + 65)
    print(result)

if __name__ == '__main__':
    problem146_b()