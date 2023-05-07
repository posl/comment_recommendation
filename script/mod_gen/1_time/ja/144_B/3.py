def main():
    N = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if i * j == N:
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()