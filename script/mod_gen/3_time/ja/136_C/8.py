def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 'Yes'
    for i in range(n - 1):
        if h[i] > h[i + 1]:
            h[i] -= 1
        if h[i] > h[i + 1]:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    main()