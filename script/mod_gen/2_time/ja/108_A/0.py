def main():
    k = int(input())
    count = 0
    for i in range(1, k + 1):
        if i % 2 == 0:
            for j in range(1, k + 1):
                if j % 2 == 1:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()