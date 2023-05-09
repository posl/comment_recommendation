def main():
    AB, CD = map(int, input().split())
    if AB * CD > 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()