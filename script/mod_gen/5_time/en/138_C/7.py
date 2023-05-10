def main():
    n = int(input())
    v = [int(i) for i in input().split()]
    v = sorted(v)
    ans = v[0]
    for i in range(1, n):
        ans = (ans + v[i]) / 2
    print(ans)

if __name__ == '__main__':
    main()