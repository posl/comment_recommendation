def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            ans = v[i]
        else:
            ans = (ans + v[i]) / 2
    print(ans)

if __name__ == '__main__':
    main()