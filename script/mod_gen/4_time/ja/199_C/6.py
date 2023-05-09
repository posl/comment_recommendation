def main():
    n = int(input())
    s = input()
    q = int(input())
    s1 = s[:n]
    s2 = s[n:]
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if a <= n and b <= n:
                s1 = s1[:a-1] + s2[b-1] + s1[a:b-1] + s2[a-1] + s1[b:]
            elif n < a and n < b:
                s2 = s2[:a-n-1] + s1[b-n-1] + s2[a-n:b-n-1] + s1[a-n-1] + s2[b-n:]
            elif n < a and b <= n:
                s2 = s2[:a-n-1] + s2[b-1] + s2[a-n:b-1] + s2[a-n-1] + s2[b:]
            elif a <= n and n < b:
                s1 = s1[:a-1] + s1[b-n-1] + s1[a:b-n-1] + s1[a-1] + s1[b-n:]
        elif t == 2:
            s1, s2 = s2, s1
    print(s1 + s2)

if __name__ == '__main__':
    main()