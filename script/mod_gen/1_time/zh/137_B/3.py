def main():
    k, x = map(int, input().split())
    for i in range(x-k+1, x+k):
        print(i, end=' ')
    print()

if __name__ == '__main__':
    main()