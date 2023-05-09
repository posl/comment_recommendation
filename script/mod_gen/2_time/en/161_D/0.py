def main():
    K = int(input())
    lunlun = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(K-1):
        x = lunlun[i]
        if x % 10 != 0:
            lunlun.append(10 * x + x % 10 - 1)
        lunlun.append(10 * x + x % 10)
        if x % 10 != 9:
            lunlun.append(10 * x + x % 10 + 1)
    print(lunlun[K-1])

if __name__ == '__main__':
    main()