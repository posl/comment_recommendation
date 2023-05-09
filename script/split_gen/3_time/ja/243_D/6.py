def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'U':
            if x % 2 == 0:
                x = x // 2
            else:
                x = (x - 1) // 2
        elif s[i] == 'L':
            x = 2 * x - 1
        else:
            x = 2 * x + 1
    print(x)
