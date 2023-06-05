def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        t = t % 3
        k = k - 1
        if t == 1:
            k = k % len(s)
            print(s[k])
        elif t == 2:
            k = k % len(s)
            print(s[k+1])
        else:
            k = k % len(s)
            print(s[k+2])

if __name__ == '__main__':
    main()