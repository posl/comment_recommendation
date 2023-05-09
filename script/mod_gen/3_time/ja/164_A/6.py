def main():
    sheep, wolf = map(int, input().split())
    if sheep >= wolf:
        print('safe')
    else:
        print('unsafe')

if __name__ == '__main__':
    main()