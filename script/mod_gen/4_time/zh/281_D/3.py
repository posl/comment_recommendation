def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    s = set()
    for i in range(n-k+1):
        s.add(sum(a[i:i+k]))
    for i in range(d):
        if i not in s:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()