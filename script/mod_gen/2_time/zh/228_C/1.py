def main():
    n, k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(sum(map(int, input().split())))
    s.sort(reverse=True)
    print("Yes" if s[k-1] > s[k] else "No")

if __name__ == '__main__':
    main()