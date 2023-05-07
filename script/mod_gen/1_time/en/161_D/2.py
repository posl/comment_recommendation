def main():
    K = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(K):
        if i < 9:
            continue
        num = lunlun[i]
        if num % 10 == 0:
            lunlun.append(num*10 + num % 10)
        elif num % 10 == 9:
            lunlun.append(num*10 + num % 10 - 1)
        else:
            lunlun.append(num*10 + num % 10)
            lunlun.append(num*10 + num % 10 - 1)
    print(lunlun[K-1])

if __name__ == '__main__':
    main()