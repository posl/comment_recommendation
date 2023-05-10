def main():
    s = input()
    result = 0
    for i in range(len(s)):
        if s[i] == '+':
            result += 1
        else:
            result -= 1
    print(result)
