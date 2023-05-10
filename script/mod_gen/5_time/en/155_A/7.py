def main():
    x = list(map(int, input().split()))
    if x[0] == x[1] and x[1] == x[2]:
        print('No')
    elif x[0] == x[1] or x[1] == x[2] or x[2] == x[0]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()