def main():
    n = int(input())
    vs = list(map(int, input().split()))
    vs.sort()
    ans = vs[0]
    for i in range(1, n):
        ans = (ans + vs[i]) / 2
    print(ans)

if __name__ == '__main__':
    main()