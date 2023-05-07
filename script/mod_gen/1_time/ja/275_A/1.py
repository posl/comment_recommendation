def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = max(H)
    for i in range(N):
        if H[i] == maxH:
            print(i+1)
            exit()

if __name__ == '__main__':
    main()