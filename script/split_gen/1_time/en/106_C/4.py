def main():
    s = input()
    k = int(input())
    if k <= len(s):
        print(s[k-1])
        return
    i = 0
    while i < len(s) and s[i] == '1':
        i += 1
    if i == len(s):
        print(1)
        return
    if s[i] == '2':
        print(2)
        return
    if s[i] == '3':
        print(3)
        return
    if s[i] == '4':
        print(4)
        return
    if s[i] == '5':
        print(5)
        return
    if s[i] == '6':
        print(6)
        return
    if s[i] == '7':
        print(7)
        return
    if s[i] == '8':
        print(8)
        return
    if s[i] == '9':
        print(9)
        return
