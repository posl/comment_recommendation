def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = []
    for i in range(k, n+1):
        ans.append(max(p[i-k:i]))
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()