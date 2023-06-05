def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    a.append(0)
    count = 0
    ans = [0] * n
    for i in range(n):
        if a[i] != a[i + 1]:
            ans[count] = i + 1
            count += 1
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()