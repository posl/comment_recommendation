def main():
    n = int(input())
    s = input()
    for i in range(1, n-1):
        if s[i] == ',' and s[i-1] != '"' and s[i+1] != '"':
            s = s[:i] + '.' + s[i+1:]
    print(s)
