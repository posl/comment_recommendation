def takoyaki_festival():
    n = int(input())
    dish = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += dish[i] * dish[j]
    print(sum)
takoyaki_festival()

if __name__ == '__main__':
    takoyaki_festival()