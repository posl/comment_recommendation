def main():
    A,B,C,D = map(int,input().split())
    count = 0
    if A <= B:
        print(-1)
    else:
        while A > B*D:
            A += B
            A -= C
            count += 1
        print(count)

if __name__ == '__main__':
    main()