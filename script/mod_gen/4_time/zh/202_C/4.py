def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = [0] * (n + 1)
    for j in c:
        d[b[j - 1]] += 1
    ans = 0
    for i in a:
        ans += d[i]
    print(ans)

if __name__ == '__main__':
    main()