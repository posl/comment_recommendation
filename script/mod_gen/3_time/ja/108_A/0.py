def main():
    K = int(input())
    count = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            if i % 2 == 0 and j % 2 != 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()