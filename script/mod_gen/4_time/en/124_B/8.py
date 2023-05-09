def main():
    N = int(input())
    H = list(map(int, input().split()))
    visible = 0
    max_height = 0
    for i in range(0, N):
        if H[i] >= max_height:
            visible += 1
            max_height = H[i]
    print(visible)

if __name__ == '__main__':
    main()