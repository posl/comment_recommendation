def main():
    N = int(input())
    H = list(map(int, input().split()))
    # 一直往右走，直到到达最右边
    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i] += 1
    print(H[-1])

if __name__ == '__main__':
    main()