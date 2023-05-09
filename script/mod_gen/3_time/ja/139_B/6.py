def main():
    A,B = map(int, input().split())
    if B <= A:
        print(1)
    else:
        if (B-A) % (A-1) == 0:
            print((B-A)//(A-1)+1)
        else:
            print((B-A)//(A-1)+2)

if __name__ == '__main__':
    main()