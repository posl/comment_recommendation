def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(1, 26):
        tmp = ''
        for c in s:
            tmp += chr((ord(c) - ord('a') + i) % 26 + ord('a'))
        if tmp == t:
            print('Yes')
            return
    print('No')
