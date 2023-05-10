def main():
    k = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(1, k):
        x = lunlun[i]
        if x % 10 == 0:
            lunlun.append(x * 10)
            lunlun.append(x * 10 + 1)
        elif x % 10 == 9:
            lunlun.append(x * 10 + 8)
            lunlun.append(x * 10 + 9)
        else:
            lunlun.append(x * 10 + x % 10 - 1)
            lunlun.append(x * 10 + x % 10)
            lunlun.append(x * 10 + x % 10 + 1)
    print(lunlun[k - 1])
