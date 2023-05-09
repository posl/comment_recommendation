def main():
    v, a, b, c = map(int, input().split())
    if (v % a) % b == 0 and (v % a) % c == 0:
        print('F')
    elif (v % a) % b == 0:
        print('T')
    elif (v % a) % c == 0:
        print('M')
    else:
        print('F')
main()

if __name__ == '__main__':
    main()