def main():
    s = input()
    k = int(input())
    l = len(s)
    i = 0
    while i < l:
        if s[i] == '1':
            i += 1
        else:
            break
    if k <= i:
        print(1)
    else:
        print(s[i])
