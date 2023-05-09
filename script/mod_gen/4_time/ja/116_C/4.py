def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    while True:
        if max(h) == 0:
            break
        for i in range(n):
            if h[i] == 0:
                continue
            else:
                h[i] -= 1
                if i == n-1:
                    count += 1
                    break
                elif i == 0:
                    if h[i+1] == 0:
                        count += 1
                        break
                elif h[i+1] == 0 and h[i-1] == 0:
                    count += 1
                    break
    print(count)

if __name__ == '__main__':
    main()