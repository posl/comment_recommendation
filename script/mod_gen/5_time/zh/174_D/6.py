def main():
    N = int(input())
    c = input()
    left = 0
    right = N - 1
    ans = 0
    while True:
        while left < N and c[left] == 'R':
            left += 1
        while right >= 0 and c[right] == 'W':
            right -= 1
        if left >= right:
            break
        ans += 1
        left += 1
        right -= 1
    print(ans)

if __name__ == '__main__':
    main()