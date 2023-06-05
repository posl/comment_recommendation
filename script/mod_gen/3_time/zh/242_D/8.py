def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        k -= 1
        for i in range(t):
            s = s[k % len(s)] + s[:k % len(s)] + s[k % len(s) + 1:]
            k = k // len(s)
        print(s[0])

if __name__ == '__main__':
    main()