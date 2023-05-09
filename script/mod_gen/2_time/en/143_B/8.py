def takoyaki_festival():
    # read the number of takoyaki
    n = int(input())
    # read the deliciousness of each takoyaki
    d = list(map(int, input().split()))
    # compute the sum of the health points restored from eating two takoyaki over all possible choices
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += d[i]*d[j]
    # print the answer
    print(sum)

if __name__ == '__main__':
    takoyaki_festival()