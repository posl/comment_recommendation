def main():
    n = int(input())
    l = []
    for i in range(60):
        if n & (1 << i):
            l.append(i)
    ans = []
    for i in range(1 << len(l)):
        x = 0
        for j in range(len(l)):
            if i & (1 << j):
                x += 1 << l[j]
        if x <= n:
            ans.append(x)
    print(*ans, sep="\n")

if __name__ == '__main__':
    main()