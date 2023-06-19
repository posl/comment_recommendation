def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    #print(x)
    sum = 0
    for i in range(n-1):
        sum += x[i+1] - x[i]
    print(sum)
main()
