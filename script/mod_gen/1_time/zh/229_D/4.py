def main():
    s = input()
    k = int(input())
    n = len(s)
    l = []
    c = 0
    for i in range(n):
        if s[i] == 'X':
            c += 1
        else:
            l.append(c)
            c = 0
    l.append(c)
    ans = 0
    for i in range(len(l)):
        if i % 2 == 0:
            ans += l[i]
    if k == 0:
        print(ans)
        return
    if len(l) % 2 == 0:
        l.append(0)
    for i in range(0, len(l), 2):
        if k == 0:
            break
        if i == 0:
            ans += l[i] + l[i + 1]
            continue
        if l[i] <= l[i - 1] + l[i + 1]:
            ans += l[i]
            continue
        ans += l[i - 1] + l[i + 1]
        ans += 1
        k -= 1
    print(ans)

if __name__ == '__main__':
    main()