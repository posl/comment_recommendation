def main():
    n = int(input())
    s = input()
    s = list(s)
    for i in range(n):
        if s[i] == '"':
            if s[i+1] == '"':
                s[i] = '.'
                s[i+1] = '.'
    print(''.join(s))
