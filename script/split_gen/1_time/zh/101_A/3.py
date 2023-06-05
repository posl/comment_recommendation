def main():
    s = input()
    num = 0
    for i in range(4):
        if s[i] == "+":
            num += 1
        else:
            num -= 1
    print(num)
