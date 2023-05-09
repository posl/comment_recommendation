def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    tmp = 0
    for i in range(n):
        if s[i] == 'X':
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    ans = max(ans, tmp)
    print(min(ans + k, n))
main()
