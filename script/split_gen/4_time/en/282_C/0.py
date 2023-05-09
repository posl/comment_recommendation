def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n):
        if s[i] == '"':
            count += 1
        if s[i] == ',' and count % 2 == 0:
            s = s[:i] + '.' + s[i+1:]
    print(s)
