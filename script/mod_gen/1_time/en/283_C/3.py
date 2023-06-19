def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        elif s[i] == '0':
            ans += 1
        elif s[i] == '1':
            ans += 2
        elif s[i] == '2':
            ans += 3
        elif s[i] == '3':
            ans += 4
        elif s[i] == '4':
            ans += 5
        elif s[i] == '5':
            ans += 6
        elif s[i] == '6':
            ans += 7
        elif s[i] == '7':
            ans += 8
        elif s[i] == '8':
            ans += 9
        elif s[i] == '9':
            ans += 10
    print(ans)
main()
