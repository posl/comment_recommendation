def solve():
    K = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(K-1):
        num = lunlun.pop(0)
        last_num = num % 10
        if last_num == 0:
            lunlun.append(num*10)
            lunlun.append(num*10+1)
        elif last_num == 9:
            lunlun.append(num*10+8)
            lunlun.append(num*10+9)
        else:
            lunlun.append(num*10+last_num-1)
            lunlun.append(num*10+last_num)
            lunlun.append(num*10+last_num+1)
    print(lunlun[0])
