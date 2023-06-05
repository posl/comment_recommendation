def main():
    line = input()
    items = line.split()
    A = int(items[0])
    B = int(items[1])
    T = int(items[2])
    count = 0
    for i in range(1,T+1):
        if i % A == 0:
            count += B
    print(count)

if __name__ == '__main__':
    main()