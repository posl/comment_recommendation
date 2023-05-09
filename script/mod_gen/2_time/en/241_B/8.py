def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = "Yes"
    i = 0
    for j in range(m):
        if i >= n:
            ans = "No"
            break
        if a[i] < b[j]:
            i += 1
            j -= 1
        elif a[i] > b[j]:
            ans = "No"
            break
    print(ans)
main()

if __name__ == '__main__':
    main()