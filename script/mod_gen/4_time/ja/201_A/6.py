def main():
    # a,b,c = map(int, input().split())
    a,b,c = map(int, input().split())
    if a-b == b-c or b-a == c-b or c-b == b-a or b-c == a-b:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()