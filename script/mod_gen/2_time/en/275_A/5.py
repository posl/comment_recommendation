def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    print(H.index(max(H))+1)

if __name__ == '__main__':
    main()