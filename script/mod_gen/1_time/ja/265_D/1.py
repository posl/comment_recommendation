def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = "No"
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] * p + a[j] * q + a[k] * r == p + q + r:
                    ans = "Yes"
                    break
    print(ans)
main()

if __name__ == '__main__':
    main()