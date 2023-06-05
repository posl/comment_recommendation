def main():
    v, a, b, c = map(int, input().split())
    v1 = v - a
    v2 = v - a - b
    v3 = v - a - b - c
    if v1 <= 0:
        print('F')
    elif v2 <= 0:
        print('M')
    else:
        print('T')

if __name__ == '__main__':
    main()