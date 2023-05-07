def main():
    #Write code here
    A, B = map(int, input().split())
    count = 1
    while A*count < B:
        count += 1
    print(count)

if __name__ == '__main__':
    main()