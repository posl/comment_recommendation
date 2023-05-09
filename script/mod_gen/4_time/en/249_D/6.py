def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] % a[j] == 0:
                for k in range(n):
                    if a[k] == a[i] / a[j]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()