def main():
    X, Y = map(int, input().split())
    if X*2 <= Y <= X*4:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()