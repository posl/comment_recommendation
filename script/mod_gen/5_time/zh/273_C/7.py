def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    i = 0
    for j in range(1, n):
        while a[i] < a[j]:
            ans[j] += 1
            i += 1
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()