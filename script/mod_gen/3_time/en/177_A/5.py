def main():
    #input
    d, t, s = map(int, input().split())
    #output
    print('Yes' if d <= t * s else 'No')

if __name__ == '__main__':
    main()