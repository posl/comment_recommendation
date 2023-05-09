def main():
    S = input()
    result = 0
    for i in S:
        if i == '+':
            result += 1
        else:
            result -= 1
    print(result)
