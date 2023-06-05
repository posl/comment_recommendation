def main():
    n = int(input())
    s = input()
    for i in range(n):
        if i % 2 == 1:
            if s[i] != '"':
                s = s[:i] + '.' + s[i+1:]
    print(s)
