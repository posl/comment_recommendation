def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    ave = sum/n
    ave = round(ave)
    sum = 0
    for i in range(n):
        sum += (a[i] - ave)**2
    print(sum)
