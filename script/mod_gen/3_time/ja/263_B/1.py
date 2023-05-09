def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    for i in range(n):
        p[i] -= 1
    ans = 0
    for i in range(n):
        c = 0
        j = i
        while j != -1:
            j = p[j]
            c += 1
        ans = max(ans, c)
    print(ans)

if __name__ == '__main__':
    main()