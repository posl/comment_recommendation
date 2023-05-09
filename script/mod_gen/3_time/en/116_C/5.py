def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while True:
        if max(h) == 0:
            break
        else:
            left = 0
            while left < N:
                if h[left] == 0:
                    left += 1
                else:
                    break
            right = left
            while right < N:
                if h[right] != 0:
                    right += 1
                else:
                    break
            for i in range(left, right):
                h[i] -= 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()