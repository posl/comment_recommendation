def main():
    n = int(input())
    count = 0
    for i in range(1, len(str(n))+1):
        if i % 3 == 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()