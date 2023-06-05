def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    ans = []
    for i in range(n):
        if a[i] in s:
            ans.append(len(s))
        else:
            ans.append(len(s) + 1)
            s.add(a[i])
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()