def main():
    n = int(input())
    v = [int(x) for x in input().split()]
    v.sort()
    ans = v[0]
    for i in range(1, n):
        ans = (ans + v[i]) / 2
    print(ans)

if __name__ == '__main__':
    main()