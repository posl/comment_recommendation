def main():
    s = input()
    if 'a' in s:
        print(s.rindex('a')+1)
    else:
        print(-1)
