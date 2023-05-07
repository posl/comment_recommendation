def main():
    n = int(input())
    s = input()
    k = 0
    for i in range(n):
        if s[i] == '"':
            k += 1
        if s[i] == ',' and k % 2 == 0:
            s = s[:i] + '.' + s[i+1:]
    print(s)
