def main():
    s = input()
    count = 0
    for i in range(0,4):
        if s[i] == '+':
            count += 1
        else:
            count -= 1
    print(count)
