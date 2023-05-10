def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max = a[-1]
    ans = 0
    for i in range(n):
        if a[i] == max:
            continue
        flag = True
        for j in range(i+1, n):
            if a[j] % a[i] == 0:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()