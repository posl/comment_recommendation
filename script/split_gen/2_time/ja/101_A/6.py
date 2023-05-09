def main():
    s = input()
    n = 0
    for i in range(4):
        if s[i] == '+':
            n += 1
        else:
            n -= 1
    print(n)
