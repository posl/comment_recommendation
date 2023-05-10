def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i*j)**(1/2) == int((i*j)**(1/2)):
                count += 1
    print(count)

if __name__ == '__main__':
    main()