def main():
    n = int(input())
    s = list(input())
    q = int(input())
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            s[a-1], s[b-1] = s[b-1], s[a-1]
        else:
            s = s[n:] + s[:n]
    print("".join(s))

if __name__ == '__main__':
    main()