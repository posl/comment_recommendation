def main():
    n = int(input())
    s = input()
    q = int(input())
    s1 = list(s[:n])
    s2 = list(s[n:])
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if a <= n and b <= n:
                s1[a-1], s1[b-1] = s1[b-1], s1[a-1]
            elif a <= n and b > n:
                s1[a-1], s2[b-n-1] = s2[b-n-1], s1[a-1]
            elif a > n and b <= n:
                s2[a-n-1], s1[b-1] = s1[b-1], s2[a-n-1]
            else:
                s2[a-n-1], s2[b-n-1] = s2[b-n-1], s2[a-n-1]
        else:
            s1, s2 = s2, s1
    print("".join(s1+s2))

if __name__ == '__main__':
    main()