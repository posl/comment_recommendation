def main():
    #输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    xy = []
    for i in range(n):
        xy.append(list(map(int, input().split())))
    #计算
    min = 0
    max = 200000
    while max - min > 0.000001:
        mid = (min + max) / 2
        #print(mid)
        #print(min)
        #print(max)
        #print("-----------")
        #print("-----------")
        #print("--

if __name__ == '__main__':
    main()