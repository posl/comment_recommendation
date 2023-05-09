def main():
    A,B,C,D = map(int,input().split())
    if A > B*D:
        print(-1)
    else:
        count = 0
        while A > B*D:
            A = A + B + C
            count = count + 1
        print(count)

if __name__ == '__main__':
    main()