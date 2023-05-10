def main():
    n = int(input())
    s = input()
    q = int(input())
    s = list(s)
    for i in range(q):
        t,a,b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            s[a],s[b] = s[b],s[a]
        else:
            s = s[n:] + s[:n]
    print("".join(s))

if __name__ == '__main__':
    main()