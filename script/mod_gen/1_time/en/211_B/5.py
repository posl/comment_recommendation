def main():
    s = [input() for _ in range(4)]
    if len(set(s)) == 4:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()