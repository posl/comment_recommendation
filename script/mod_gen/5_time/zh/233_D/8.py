def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    left = 0
    right = 0
    s = a[0]
    ans = 0
    while left < n:
        if s == k:
            ans += 1
            s -= a[left]
            left += 1
            if right < left:
                right = left
                s = a[left]
        elif s < k:
            right += 1
            if right < n:
                s += a[right]
            else:
                break
        else:
            s -= a[left]
            left += 1
            if right < left:
                right = left
                s = a[left]
    print(ans)

if __name__ == '__main__':
    main()