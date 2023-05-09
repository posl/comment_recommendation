def main():
    inputs = input().rstrip().split()
    m = int(inputs[0])
    h = int(inputs[1])
    if h % m == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()