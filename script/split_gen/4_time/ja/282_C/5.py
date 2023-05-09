def main():
    n = int(input())
    s = input()
    s = list(s)
    cnt = 0
    for i in range(n):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',' and cnt % 2 == 1:
            s[i] = '.'
    print(''.join(s))
