def main():
    N = int(input())
    count = 0
    for i in range(1,N):
        for j in range(1,N):
            if i*j < N:
                count += 1
    print(count)

if __name__ == '__main__':
    main()