def main():
    N = int(input())
    H = input().split()
    H = list(map(int, H))
    print(H.index(max(H))+1)

if __name__ == '__main__':
    main()