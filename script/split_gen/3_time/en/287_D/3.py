def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i].replace('?', '') + s[-(len(t)-i):].replace('?', '') == t:
            print('Yes')
        else:
            print('No')
