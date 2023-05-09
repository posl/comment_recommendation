def main():
    s = input()
    if s[0] == 'o':
        n = 9
    elif s[0] == 'x':
        n = 0
    else:
        n = 10
    for i in range(1, 10):
        if s[i] == 'o':
            n *= 9 - i
        elif s[i] == 'x':
            n *= i
        else:
            n *= 10 - i
    print(n)
