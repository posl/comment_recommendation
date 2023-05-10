def main():
    k = int(input())
    lunlun_list = [i for i in range(1,10)]
    if k <= 9:
        print(lunlun_list[k-1])
    else:
        k -= 9
        while k > 0:
            new_lunlun_list = []
            for lunlun in lunlun_list:
                last_digit = lunlun % 10
                if last_digit == 0:
                    new_lunlun_list.append(lunlun * 10)
                    new_lunlun_list.append(lunlun * 10 + 1)
                elif last_digit == 9:
                    new_lunlun_list.append(lunlun * 10 + last_digit - 1)
                    new_lunlun_list.append(lunlun * 10 + last_digit)
                else:
                    new_lunlun_list.append(lunlun * 10 + last_digit - 1)
                    new_lunlun_list.append(lunlun * 10 + last_digit)
                    new_lunlun_list.append(lunlun * 10 + last_digit + 1)
            lunlun_list = new_lunlun_list
            k -= len(lunlun_list)
        print(lunlun_list[k-1])

if __name__ == '__main__':
    main()