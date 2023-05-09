def main():
    n = int(input())
    a = [0] * (n-1)
    b = [0] * (n-1)
    for i in range(n-1):
        a[i], b[i] = map(int, input().split())
    ans = "Yes"
    for i in range(n-1):
        if a[i] == 1 or b[i] == 1:
            continue
        else:
            ans = "No"
            break
    print(ans)

if __name__ == '__main__':
    main()