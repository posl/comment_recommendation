def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        for j in range(i,N+1):
            if (i*j)**0.5 == int((i*j)**0.5):
                count += 1
    print(count)

if __name__ == '__main__':
    main()