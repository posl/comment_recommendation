def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(k):
        t2 = t[i::k]
        t3 = t2.replace('r', 'p').replace('s', 'r').replace('p', 's')
        t4 = t3.replace('p', 'r')
        ans += t4.count('r') * r + t4.count('s') * s + t4.count('p') * p
    print(ans)

if __name__ == '__main__':
    main()