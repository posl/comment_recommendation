def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    last = 0
    for a, b in AB:
        if a <= last:
            continue
        else:
            last = b - 1
            ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()