def main():
    N = int(input())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
    ans = "Yes"
    for i in range(N-1):
        if a.count(a[i]) + a.count(b[i]) != 1:
            ans = "No"
            break
        if b.count(a[i]) + b.count(b[i]) != 1:
            ans = "No"
            break
    print(ans)

if __name__ == '__main__':
    main()