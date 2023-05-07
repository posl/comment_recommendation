def takoyaki_festival():
    N = int(input())
    d = [int(x) for x in input().split()]
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d[i] * d[j]
    print(sum)

if __name__ == '__main__':
    takoyaki_festival()