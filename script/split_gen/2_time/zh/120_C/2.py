def main():
    s = input()
    n = len(s)
    red = 0
    blue = 0
    for i in range(n):
        if s[i] == '0':
            red += 1
        else:
            blue += 1
    print(n - abs(red - blue))
