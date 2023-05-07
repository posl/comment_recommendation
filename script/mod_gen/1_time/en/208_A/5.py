def main():
    A, B = map(int, input().split())
    for i in range(A+1):
        for j in range(A+1):
            if 6*i+1*j == B:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()