def main():
    s = input()
    result = 0
    for i in s:
        if i == "+":
            result += 1
        else:
            result -= 1
    print(result)
