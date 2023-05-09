def main():
    s = input()
    if 'a' not in s:
        print(-1)
    else:
        print(len(s) - s[::-1].index('a'))
