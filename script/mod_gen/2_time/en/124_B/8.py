def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(len([i for i in range(1, N) if H[i-1] <= H[i]]))

if __name__ == '__main__':
    main()