def main():
    N, M = map(int, input().split())
    for i in range(1, M+1):
        if i > N:
            print(i)
        else:
            print(i, end=' ')

if __name__ == '__main__':
    main()