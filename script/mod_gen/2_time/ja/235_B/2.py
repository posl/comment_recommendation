def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_H = 0
    for i in range(N):
        if H[i] >= max_H:
            max_H = H[i]
    print(max_H)

if __name__ == '__main__':
    main()