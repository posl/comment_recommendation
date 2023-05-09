def main():
    n = int(input())
    lunlun_num = [i for i in range(1, 10)]
    for i in range(n):
        lunlun_num.append(lunlun_num[i]*10+lunlun_num[i]%10)
        if lunlun_num[i]%10 != 0:
            lunlun_num.append(lunlun_num[i]*10+lunlun_num[i]%10-1)
        if lunlun_num[i]%10 != 9:
            lunlun_num.append(lunlun_num[i]*10+lunlun_num[i]%10+1)
    lunlun_num.sort()
    print(lunlun_num[n-1])

if __name__ == '__main__':
    main()