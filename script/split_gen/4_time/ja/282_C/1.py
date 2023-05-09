def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',' and cnt % 2 == 0:
            s = s[:i] + '.' + s[i+1:]
    print(s)
