def main():
    K = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(1, K):
        n = lunlun[i]
        last = n % 10
        if last > 0:
            lunlun.append(n * 10 + last - 1)
        lunlun.append(n * 10 + last)
        if last < 9:
            lunlun.append(n * 10 + last + 1)
    print(lunlun[K - 1])
main()

if __name__ == '__main__':
    main()