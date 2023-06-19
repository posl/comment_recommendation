def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = 0
    res = 0
    for i in range(N):
        if H[i] >= max_h:
            res += 1
            max_h = H[i]
    print(res)

if __name__ == '__main__':
    main()