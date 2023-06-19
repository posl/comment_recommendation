def main():
    n, x = map(int, input().split())
    s = input()
    x = x - 1
    for i in range(n):
        if s[i] == 'L':
            x = x * 2
        elif s[i] == 'R':
            x = x * 2 + 2
        else:
            x = x * 2 + 1
    print(x + 1)
