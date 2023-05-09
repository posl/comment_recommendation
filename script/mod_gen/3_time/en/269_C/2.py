def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = []
    for i in range(1 << 15):
        x = 0
        for j in range(15):
            if i & (1 << j):
                x += 2 ** j
        if x <= n:
            ans.append(x)
    ans.sort()
    print(*ans, sep="\n")

if __name__ == '__main__':
    main()