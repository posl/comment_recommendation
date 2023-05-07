def main():
    K = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(1, K):
        num = lunlun[i]
        last = num % 10
        if last == 0:
            lunlun.append(num * 10 + last)
            lunlun.append(num * 10 + last + 1)
        elif last == 9:
            lunlun.append(num * 10 + last - 1)
            lunlun.append(num * 10 + last)
        else:
            lunlun.append(num * 10 + last - 1)
            lunlun.append(num * 10 + last)
            lunlun.append(num * 10 + last + 1)
    print(lunlun[K-1])
