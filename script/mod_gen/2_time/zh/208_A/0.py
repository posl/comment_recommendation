def main():
    a,b = map(int, input().split())
    for i in range(1, a+1):
        for j in range(1, a+1):
            if i+j == b:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    main()