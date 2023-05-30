def lunlun(k):
    lunlun_list = [1,2,3,4,5,6,7,8,9]
    for i in range(1, 11):
        for j in range(-1, 2):
            if lunlun_list[i] % 10 + j >= 0 and lunlun_list[i] % 10 + j <= 9:
                lunlun_list.append(lunlun_list[i] * 10 + lunlun_list[i] % 10 + j)
    print(lunlun_list[k-1])
k = int(input())
lunlun(k)
