def main():
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == ',':
            if (i+1) % 2 == 0:
                s = s[:i] + '.' + s[i+1:]
    print(s)
