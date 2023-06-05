def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = H[0]
    for i in range(1, N):
        if H[i] >= max_h:
            max_h = H[i]
    print(max_h)

if __name__ == '__main__':
    main()