def main():
    a, b, c = map(int, input().split())
    array = [a, b, c]
    array.sort()
    if array[1] == b:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()