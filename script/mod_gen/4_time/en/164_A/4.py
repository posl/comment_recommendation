def main():
    sheep, wolves = map(int, input().split())
    if wolves >= sheep:
        print('unsafe')
    else:
        print('safe')

if __name__ == '__main__':
    main()