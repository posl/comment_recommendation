def main():
    s = input()
    result = 0
    for i in range(4):
        if s[i] == "+":
            result += 1
        else:
            result -= 1
    print(result)
