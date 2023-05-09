def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    s = [a[0]]
    for i in range(1, n):
        if a[i] < s[-1]:
            s.append(a[i])
        else:
            s.append(s[-1])
    s.reverse()
    ans = 0
    for i in range(n):
        ans += s[i] - a[i]
    print(ans)
main()

if __name__ == '__main__':
    main()