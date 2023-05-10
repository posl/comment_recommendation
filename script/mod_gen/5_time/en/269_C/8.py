def main():
    n = int(input())
    k = len(bin(n))-2
    l = [i for i in range(k) if n&(1<<i)]
    if not l:
        print(0)
        return
    ans = []
    for i in range(1<<len(l)):
        x = 0
        for j in range(len(l)):
            if i&(1<<j):
                x += 1<<l[j]
        if x<=n:
            ans.append(x)
    ans.sort()
    for i in ans:
        print(i)
main()

if __name__ == '__main__':
    main()