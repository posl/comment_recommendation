def main():
    n = int(input())
    s = input()
    a = []
    for i in range(len(s)):
        a.append(chr(ord(s[i])+n))
        if ord(a[i]) > 90:
            a[i] = chr(ord(a[i])-26)
    print(''.join(a))
