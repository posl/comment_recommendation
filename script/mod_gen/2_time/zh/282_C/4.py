def main():
    n = int(input())
    s = input()
    s = list(s)
    for i in range(1, n+1):
        if i % 2 == 0:
            continue
        if s[i-1] != '"' and s[i] != '"':
            s[i-1] = '.'
    print(''.join(s))
main()
