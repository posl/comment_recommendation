def main():
    a,b,c = map(int,input().split())
    if b in [a,c]:
        print('是')
    else:
        print('没有')

if __name__ == '__main__':
    main()