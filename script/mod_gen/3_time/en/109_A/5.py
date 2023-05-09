def main():
    A,B = [int(x) for x in input().split()]
    for C in range(1,4):
        if (A*B*C)%2 == 1:
            print('Yes')
            return
    print('No')
    return

if __name__ == '__main__':
    main()