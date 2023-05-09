def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(H.index(max(H)) + 1)

if __name__ == '__main__':
    main()