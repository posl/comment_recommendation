def main():
    S = input()
    count = 0
    for i in S:
        if S.count(i) == 2:
            count += 1
    if count == 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()